def caesar_encrypt(word, step):
    if not type(word) is str:
        raise TypeError("'\'word\' argument must be a string")
    if not type(step) is int:
        raise TypeError("\'step\' argument must be an integer")
    
    encrypted_word = ''
    for char in word:
        if char is ' ':
            encrypted_word += ' '
        elif char.isupper():
            encrypted_word += chr((ord(char) + step - 65) % 26 + 65)
        else:
            encrypted_word += chr((ord(char) + step - 97) % 26 + 97)
    print(encrypted_word)


caesar_encrypt("treaty impossible", 3)
