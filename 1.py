def palindrome(word):
    word=word
    newword=word[::-1]
    if newword==word:
        print(f"{newword} is a palindrome")
    else:
        print(f"{newword} is not a palindrome")
palindrome("malayalam")