# 6320500719 นายอัษฎาวุธ คล้ายเมือง

def encrypt(p, k):
    b = text_to_binary(p)
    secret_key_binary = k.replace(' ', '')

    encrypted_binary = ''
    for i in range(len(b)):
        ch1 = b[i]
        ch2 = secret_key_binary[i]
        encrypted_ch = str(int(ch1) ^ int(ch2))
        encrypted_binary += encrypted_ch

    t = binary_to_text(encrypted_binary)
    t = t.upper()
    return t


def decrypt(t, k):
    t = text_to_binary(t)
    secret_key_binary = k.replace(' ', '')

    decrypted_binary = ''
    for i in range(len(t)):
        ch1 = t[i]
        ch2 = secret_key_binary[i]
        decrypted_ch = str(int(ch1) ^ int(ch2))
        decrypted_binary += decrypted_ch

    decrypted_text = binary_to_text(decrypted_binary)
    decrypted_text = decrypted_text.upper()
    return decrypted_text

def text_to_binary(text):
    binary_text = ''
    for char in text:
        if char.isalpha():
            char_index = ord(char) - ord('A')
            binary_text += format(char_index, '05b')
    return binary_text


def binary_to_text(binary_text):
    text = ''
    for i in range(0, len(binary_text), 5):
        binary_char = binary_text[i:i + 5]
        char_index = int(binary_char, 2)
        char = chr(char_index + ord('A'))
        text += char
    return text

print("Welcome to A One-time Pad")
progress_type = input("Enter type (E/D): ").upper()

if progress_type == "E":
    p = input("Enter string: ").upper()
    secret_key = input("Enter key string (5-bit binary with spaces): ")
    encrypted_text = encrypt(p, secret_key)
    print(f"String output is {encrypted_text}")

elif progress_type == "D":
    encrypted_text = input("Enter string: ").upper()
    secret_key = input("Enter key string (5-bit binary with spaces): ")
    decrypted_text = decrypt(encrypted_text, secret_key)
    print(f"String output is {decrypted_text}")

else:
    print("Invalid input. Please enter 'E' for encryption or 'D' for decryption.")