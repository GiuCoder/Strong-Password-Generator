import os

os.system("echo Importing All Modules >> temp.txt")
import platform
import random
import string
import time

from tqdm import tqdm

characters = string.ascii_letters + string.digits + string.ascii_uppercase

# USERNAME
os.system("echo Program has been started >> temp.txt")
username = input("Enter Username :  ")
os.system(f"echo Client Username : {username} >> temp.txt")

os.system("cls")
os.system("echo Creating Username Data ...  >> temp.txt")
# Open a file for writing and write the username to it
with open('username.txt', 'w') as f:
    f.write(username)
# Open the file for reading and read the username from it

with open('username.txt', 'r') as f:
    username = f.read()

os.system("echo Username has been created and can read only >> temp.txt")
os.system("echo Checking User Platform ... >> temp.txt")
os_name = platform.system()
os.system(f"echo User Platform : {os_name}")
if os_name == "Windows":
    os.system("cls")
    os.system("echo Print Has Been Executed >> temp.txt")
    print(f"Hi {username}...\nLoading Tools ...\n")
    time.sleep(5)
    os.system("echo Create Random Num With random.uniform(0, 0.8) >> temp.txt")
    random_num = random.uniform(0, 0.8)
    os.system("echo Loading Animation From TDQM! >> temp.txt")
    for i in tqdm(range(100), desc="Downloading Data ", ascii=False, ncols=75):
        time.sleep(random_num)
    # Start Make Password
    os.system("cls")
    time.sleep(2)
    os.system("echo Settings User Input >> temp.txt")
    # Leng of password
    os.system("echo Running User Input >> temp.txt")
    Length = input("Length : ")
    os.system("echo Checking Length ... >> temp.txt")
    if Length == "":
        os.system("cls")
        os.system("echo Length Input Is Null >> temp.txt")
        print("Please Enter A Valid Length!\n")
        os.system("echo Requesting rerun to client!!! >> temp.txt")
        leave = input("Do You Want To ReRun The Program Y/N : ")
        if leave == "Y" or "y" or "yes" or "YES" or "Yes" or "YEs":
            os.system("echoUser Accepted\nRunning Start Main.py >> temp.txt")
            os.system("start main.py")
            os.system("echo Running Success >> temp.txt")
        elif leave == "N" or "NO" "No" or "n" or "nO":
            os.system("echo Clien Reject\nExiting With Code 12 >> temp.txt")
            exit(12)
    os.system("echo Set Length For Generating Passwords >> temp.txt")
    length = int(Length)

    # Generate the random string
    random_password = ''.join(random.choice(characters) for i in range(length))
    time.sleep(2)
    os.system("cls")
    # Start Password
    os.system("echo Start Generating Password >> temp.txt")
    for i in tqdm(range(100), desc="Generating Strong Password ", ascii=False, ncols=75):
        time.sleep(0.3)
    time.sleep(5)
    # Generate Password
    # Save password to a file
    os.system("echo Request Client Input File Name >> temp.txt")
    file_name = input("File Name To Save Your Password (JUST ENTER FILE NAME || EX : MY_PASSWORD): ")
    with open(file_name + ".txt", 'w') as f:
        print(random_password.strip(), file=f)
        os.system(f"echo Password will saved to {file_name}")

    # Notify the user that the password has been saved to a file
    os.system("echo Password Saved >> temp.txt")

    print(f"echo Password saved to file {file_name}\n\n >> temp.txt")
    os.system("pause")
    os.system("echo Clossing Teminal and Aborting OS ... >> temp.txt")
    os.abort()
    os.system("echo Terminal Shutted Down >> temp.txt")
    exit()

else:
    os.system(f"echo Failed to run program because clien run on platform {os_name}")
    print("You Can Only Run This Program On Windows")
    os.system("echo Clossing Teminal and Aborting OS ... >> temp.txt")
    os.abort()
    os.system("Terminal Shutted Down >> temp.txt")
    exit(10)
