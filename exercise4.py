message = input('> ')
words = message.split(' ')

emoji_conversion = {
    ':)': '😀',
    ':(': '😔',
    '<3': '❤',
}
output = ''

for word in words:
    output += emoji_conversion.get(word, word) + " "

print(output)