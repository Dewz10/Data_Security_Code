# 6320500719 นายอัษฎาวุธ คล้ายเมือง
import math

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Welcome to RSA!")

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

n = p * q
print(f"The value of n is {p}x{q}={n}")

z = (p - 1) * (q - 1)

e = int(input(f"Enter co-prime e ]1,{z}[: "))
while math.gcd(e, z) != 1:
    print(f"Sorry! {e} is not co-prime of ({p}-1)({q}-1)={z}.")
    e = int(input(f"Enter co-prime e ]1,{z}[: "))

d = pow(e, -1, z)

progress_type = input("Enter the progress type E/D: ")

if progress_type == "D":
    c = input("Enter the ciphertext: ")
    ciphertext = ""
    for i in c.split("-"):
        c = pow(int(i), d, n)
        ciphertext += alphabet[c]
    print(f"The private key d is {d}")
    print(f"The ciphertext is {ciphertext}")
elif progress_type == "E":
    plaintext = input("Enter the plaintext: ")
    ciphertext = ""
    for char in plaintext:
        c = pow(alphabet.find(char), e, n)
        ciphertext += str(c) + "-"
    ciphertext = ciphertext[:-1]
    print(f"The plaintext is {ciphertext}")
else:
    print("Invalid progress type. Please enter 'E' for encryption or 'D' for decryption.")