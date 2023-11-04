# 6320500719 นายอัษฎาวุธ คล้ายเมือง
def find_char(letter, fc_alpha):
    result = -1
    for i in range(len(fc_alpha)):
        if letter == fc_alpha[i]:
            result = i
            break
    return result


def encryption(en_msg, en_alpha, en_encrypt_keys):
    length = len(en_msg)
    encrypted_msg = [''] * (length + 1)
    for i in range(length):
        if en_msg[i] != ' ':
            letter = en_msg[i].upper()
            result_index = find_char(letter, en_alpha)
            key_index = i % len(en_encrypt_keys)
            encrypted_msg[i] = en_encrypt_keys[key_index][result_index]
        else:
            encrypted_msg[i] = en_msg[i]
        encrypted_msg[length] = ''
    return ''.join(encrypted_msg)


def decryption(de_msg, de_alpha, de_decrypt_keys):
    length = len(de_msg)
    decrypted_msg = [''] * (length + 1)
    for i in range(length):
        if de_msg[i] != ' ':
            letter = de_msg[i].upper()
            result = -1
            key_index = i % len(de_decrypt_keys)
            result = find_char(letter, de_decrypt_keys[key_index])
            if result != -1:
                decrypted_msg[i] = de_alpha[result]
            else:
                decrypted_msg[i] = letter
        else:
            decrypted_msg[i] = de_msg[i]
    return ''.join(decrypted_msg)


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Welcome to A Polyalphabetic Substitution Cipher")

# Validate the choice input
while True:
    choice = input("Enter type (E/D): ").upper()  # Convert input to uppercase for case-insensitivity
    if choice in ['E', 'D']:
        break
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

message = input("Enter string: ")
num_keys = int(input("Enter a number of keys: "))
encrypt_keys = []

for i in range(num_keys):
    key_string = input(f"Enter {i + 1}-key string: ")
    encrypt_keys.append(key_string)

if choice == 'E':
    encrypt = encryption(message, alpha, encrypt_keys)
    print(f"Encrypted: {encrypt}")
elif choice == 'D':
    if len(encrypt_keys) != num_keys:
        print("Invalid number of keys. Please provide the correct number of keys.")
    else:
        decrypt = decryption(message, alpha, encrypt_keys)
        print(f"Decrypted: {decrypt}")
