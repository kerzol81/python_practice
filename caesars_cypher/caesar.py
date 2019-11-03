def caesar_encrypt(word, step):
    if not type(word) is str:
        raise TypeError("\'word\' argument must be a string")
    if not type(step) is int:
        raise TypeError("\'step\' argument must be an integer")
    print(word)
    result = ""
    for char in word:
        if char is ' ':
            result += ' '
        if char.isupper():
            result += chr((ord(char) + step - 65) % 26 + 65)
        else:
            result += chr((ord(char) + step - 97) % 26 + 97)
    print(result)


caesar_encrypt("treaty impossible", 3)
