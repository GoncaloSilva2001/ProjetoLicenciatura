import emoji

def convert_emoji_to_text(emoji_text):
    text_with_aliases = emoji.demojize(emoji_text)
    return text_with_aliases


if __name__ == "__main__":
    emoji_text = "I love Python! 😍🐍"
    converted_text = convert_emoji_to_text(emoji_text)
    print("Original text:", emoji_text)
    print("converted text:", converted_text)
