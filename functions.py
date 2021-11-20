message = input('> ')
emoji_conversion = {
    ':)': '😀',
    ':(': '😔',
    '<3': '❤',
}

def emoji_converter(msg):
    words = msg.split(' ')
    output = ''

    for word in words:
        output += emoji_conversion.get(word, word) + " "
    return output


result = emoji_converter(message)
print(result)