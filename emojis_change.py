import requests
from bs4 import BeautifulSoup
from typing import List
from unicodedata import normalize

def fetch_emojis(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        emojis = soup.find_all('span', class_='emoji emoji-large')
        emoji_list = [emoji.text.strip() for emoji in emojis]
        return emoji_list
    else:
        print(f"Failed to fetch emojis. Status code: {response.status_code}")
        return []

def get_unicode_code_points(string: str) -> List[str]:
    string_normalized = normalize('NFD', string)
    code_points: List[str] = [
        'U+' + hex(ord(letter))[2:].zfill(4).upper()
        for letter in string_normalized
    ]
    return code_points

if __name__ == "__main__":
    url = "https://getemoji.com/"
    emojis = fetch_emojis(url)
    print("Emojis found on the page:")
    for emoji in emojis:
        code_points = get_unicode_code_points(emoji)
        print(f"Emoji: {emoji} | Unicode: {' '.join(code_points)}")