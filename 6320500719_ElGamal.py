# 6320500719 นายอัษฎาวุธ คล้ายเมือง

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Welcome to ElGamal Cryptosystem!")

p = int(input("Enter prime p: "))
g = int(input(f"Enter co-prime g [1, {p-1}]: "))
x = int(input(f"Enter private key x ]1, {p-1}[: "))
# Public key
y = pow(g, x, p)

print("Enter public key y is", y)

prgress_type = input("Enter the progress type E/D: ").upper()

if prgress_type == "E":
    # Encryption
    plaintext = input("Enter the plaintext: ")
    k = int(input("The random number k is "))
    c1 = pow(g, k, p)
    c2 = (alphabet.find(plaintext) * pow(y,k)) % p
    print("The ciphertext 1 is", c1)
    print("The ciphertext 2 is", c2)

elif prgress_type == "D":
    # Decryption
    ciphertext1 = int(input("Enter the ciphertext 1: "))
    ciphertext2 = int(input("Enter the ciphertext 2: "))
    decrypted = (ciphertext2 * pow(ciphertext1, -x, p)) % p
    print("The plaintext is", alphabet[decrypted])

else:
    print("Invalid progress type. Please enter 'E' for encryption or 'D' for decryption.")
