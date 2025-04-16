import random

# =============================== 🔐 Secure Password Generator | Crafted by Muzna Amir Zubairi ===============================

print("⏳ Welcome to the Password Generator App | Developed by Muzna Amir Zubairi")

given_char = "!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678910abcdefghijklmnopqrstuvwxyz"

num = input("Enter your number : ")
num = int(num)


length = input("Enter your password length : ")
length = int(length)
print("\n")

print("Here is your password : ")

for p in range(num):
    password = ""
    for l in range(length):
        password += random.choice(given_char)
    print(password)
