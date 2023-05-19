import random
from cryptography.fernet import Fernet
import os

chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1', '2', '3', '4', '5', '6', '7', '8', '9', '10','!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']


def createBanner(text):
    banner = f'''
    #===========================================#
    |                                           |
    |               {text}         |
    |                                           |
    #===========================================#
    '''
    return banner

# Usage example
banner_text = "Password Generater!"
banner = createBanner(banner_text)
print(banner + "\n\n")



file_path = input('[+]Enter file path (e.g driveLetter:\\UserName\\UserName\\Desktop\\Destination): ')
pass_length = int(input('[+]Enter length of password: '))
account_name = input('[+]What is the password for? ')

#---------------------------GENERATING A PASSWORD
def generate_pass(x_value):
    password_characters = []
    while len(password_characters) != x_value:
        selection = random.choice(chars)
        password_characters.append(selection)

    password = ''.join(password_characters)
    return password

#---------------------------ENCRYPTING THE PASSWORD
def enCrypt_text(text, key):
    fernette = Fernet(key)
    enCrypted_pass = fernette.encrypt(text.encode())
    return enCrypted_pass

f_key = Fernet.generate_key()
password = generate_pass(pass_length)

enCrypted_pass = {account_name,enCrypt_text(password, f_key)}
enCrypted_pass_str = str(enCrypted_pass)

#-------------------------WRITING TO A FILE
with open(f'{file_path}\GeneratedPasswords.txt', 'a') as file:
        file.write(enCrypted_pass_str)
