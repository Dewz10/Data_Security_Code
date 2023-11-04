# 6320500719 นายอัษฎาวุธ คล้ายเมือง
def caesar_cipher(text, key, action):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                shift = ord('A')
            else:
                shift = ord('a')
            result += chr(((ord(char) - shift + key) % 26) + shift)
        else:
            result += char

    return result


def main():
    print("Welcome to the Caesar Cipher")
    action = input("Enter type (E/D): ").upper()

    if action not in ['E', 'D']:
        print("Invalid action. Please enter 'E' for encryption or 'D' for decryption.")
        return

    text = input("Enter string: ")
    key = int(input("Enter key: "))

    if action == 'E':
        output = caesar_cipher(text, key, 'E')
        print("String output is:", output)
    else:
        output = caesar_cipher(text, -key, 'D')
        print("String output is:", output)


if __name__ == "__main__":
    main()
