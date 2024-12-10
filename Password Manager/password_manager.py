

import os
from cryptography.fernet import Fernet




folder_path = r'C:\Users\_akshay_0452\Desktop\python\Python-Projects\Password Manager'

key_path = os.path.join(folder_path, 'key.key')

'''
def write_key():
    key = Fernet.generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

'''


# write_key()

def load_key():
    file = open(key_path, "rb")
    key = file.read()
    file.close()
    return key



pwd_master = input("what is your master password?  ")

key = load_key()
fer = Fernet(key)



file_path = os.path.join(folder_path, 'passwords.txt')


def view():
    try:
        with open(file_path, 'r') as f:
            for line in f.readlines():
                data = line.strip()  # Remove extra whitespace
                if "|" not in data:
                    print(f"Skipping malformed line: {data}")
                    continue  # Skip lines that do not contain "|"
                try:
                    user, passw = data.split("|", 1)  # Split into user and password
                    decrypted_password = fer.decrypt(passw.encode()).decode()
                    print(f"User: {user} | Password: {decrypted_password}")
                except Exception as e:
                    print(f"Error decrypting line: {data}. Error: {e}")
    except FileNotFoundError:
        print("No password file found. Add some passwords first!")

def add():
    
    print("Enter the account name: ")
    name = input()

    print("Pasword of the account : ")
    pwd = input()

    with open(file_path, 'a') as f:
        f.write(name + ' | ' + fer.encrypt(pwd.encode()).decode() + '\n')



while True:
    mode = input("would you like to add or view existing ones (view, add), press q to quit! ").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()

    elif mode == 'add':
        add()

    else :
        print("Invalid mode !")