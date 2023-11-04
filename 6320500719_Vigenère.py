# 6320500719 นายอัษฎาวุธ คล้ายเมือง

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def vigenere_cipher(text, key, mode):
    text = text.replace(" ", "")
    result = ""
    kl = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_ch = key[i % kl]
            if char.islower():
                shift = ord('a')
            else:
                shift = ord('A')
            if mode == 'E':
                ch_index = alphabet.index(char.upper())
                key_index = alphabet.index(key_ch.upper())
                index = (ch_index + key_index) % 26
                result += alphabet[index]
            elif mode == 'D':
                ch_index = alphabet.index(char.upper())
                key_index = alphabet.index(key_ch.upper())
                index = (ch_index - key_index) % 26
                result += alphabet[index]
        else:
            result += char
    return result

print("Welcome to the Vigenère Cipher")

while True:
    mode = input("Enter type (E/D): ").upper()
    if mode not in ('E', 'D'):
        print("Invalid mode. Please enter 'E' for encryption or 'D' for decryption.")
    else:
        break

text = input("Enter string: ")
key = input("Enter key string: ")

encrypted_text = vigenere_cipher(text, key, mode)

print("String output is:", encrypted_text)
