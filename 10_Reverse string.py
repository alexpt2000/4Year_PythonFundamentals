def reverse(word):
    wordNew = ''
    index = len(word)
    while index:
        index -= 1
        wordNew += word[index]
    return wordNew

word = str(input('Enter the string: '))

print(reverse(word))
