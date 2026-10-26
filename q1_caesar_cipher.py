ciphertext = input("Enter ciphertext: ")

for key in range(26):
    plaintext = ""

    for char in ciphertext:
        if char.isupper():
            plaintext += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        elif char.islower():
            plaintext += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            plaintext += char

    print(chr(key + ord('A')), plaintext)