message = input(">")

message_parts = message.split(' ')


emojis = {
    ":)": "😊",
    ":(": "😓" 
}

output = ""
for word in message_parts:
    output += emojis.get(word, word) + ' '
print(output)