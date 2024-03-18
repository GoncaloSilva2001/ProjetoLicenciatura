import requests
from bs4 import BeautifulSoup
import emoji
import json
from openpyxl import Workbook

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

def get_unicode_code_points(string):
    return ' '.join([f'U+{ord(char):X}' for char in string])

def get_emoji_description(emoji_char):
    shortcode = emoji.demojize(emoji_char)

    return shortcode

if __name__ == "__main__":
    url = "https://getemoji.com/"
    emojis = fetch_emojis(url)

    data_for_xlsx = [['Emoji', 'Unicode', 'Description']]

    for emoji_char in emojis:
        unicode_points = get_unicode_code_points(emoji_char)
        shortcode = get_emoji_description(emoji_char)
        data_for_xlsx.append([emoji_char, unicode_points, shortcode])

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Emojis"

    # Write data to worksheet
    for row in data_for_xlsx:
        ws.append(row)

    # Save workbook to XLSX file
    wb.save("emojis.xlsx")

    # Save data to JSON
    with open('emojis.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(data_for_xlsx[1:], jsonfile, indent=4)
