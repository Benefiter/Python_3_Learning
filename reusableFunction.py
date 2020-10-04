def emoji_convert(text_emoji):
    emojis = {
        ":)": "😊",
        ":(": "😓" 
    }
    return emojis.get(text_emoji, text_emoji)


def get_message_with_emojis(message):
    message_parts = message.split(' ')

    output = ""
    for word in message_parts:
        output += emoji_convert(word) + ' '
    return output


message = input(">")

print(get_message_with_emojis(message))