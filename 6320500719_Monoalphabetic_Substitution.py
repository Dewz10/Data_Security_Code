# 6320500719 นายอัษฎาวุธ คล้ายเมือง
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(text, key):
    new = []
    for letter in text:
        if letter in alpha:
            new.append(key[alpha.index(letter)])
        else:
            new.append(letter)

    return "".join(new)


def decrypt(cipher, key):
    new = []
    for letter in cipher:
        if letter in key:
            new.append(alpha[key.index(letter)])
        else:
            new.append(letter)

    return "".join(new)


def is_valid_key(key):
    # Check if the key contains all uppercase letters A-Z with no duplicates.
    return len(key) == 26 and all(c.isalpha() and c.isupper() for c in key) and len(set(key)) == 26


def main():
    print("Welcome to A Mono-alphabetic Substitution Cipher")
    choice = input("Enter type (E/D): ").strip().upper()

    if choice == 'E':
        text = input("Enter string: ").upper()
        key = input("Enter key string [A-Z]: ").upper()

        if is_valid_key(key):
            e = encrypt(text, key)
            print(f"String output is: {e}")
        else:
            print("Invalid key. The key must contain all uppercase letters A-Z with no duplicates.")
    elif choice == 'D':
        cipher = input("Enter cipher: ").upper()
        key = input("Enter key string [A-Z]: ").upper()

        if is_valid_key(key):
            d = decrypt(cipher, key)
            print(f"String output is: {d}")
        else:
            print("Invalid key. The key must contain all uppercase letters A-Z with no duplicates.")
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")


if __name__ == "__main__":
    main()
