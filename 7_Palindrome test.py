def testPalidrome(test):
    test = word[::-1] == word[::1]  # Logical test (True and False)
    return test

word = str(input("input the word: "))

if testPalidrome(word) == True:
    print("Is Palindrome")

else:
    print("Not Palindrome")



