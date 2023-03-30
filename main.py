import os
import time
print("1. Make Password\n2. Exit\n\n")
choice = input("Enter Choice : ")
if choice == "1":
    os.system("start generator.py")


if choice == "2":
    print("GoodBye :)\n")
    exit(10)

if choice=="":
    print("Invalid Choice")
    input("")
    os.system("start main.py")
    exit()