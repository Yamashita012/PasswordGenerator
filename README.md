# PasswordGenerator
 The provided Python script is a password generator that utilizes the Fernet encryption algorithm for secure password storage. It allows users to generate random passwords of specified lengths, encrypt them, and store the encrypted passwords in a designated file.

## Prerequisites
Make sure you have the following libraries installed:
- random
- cryptography

You can install the required libraries using pip:
```
pip install cryptography
```

## Usage
1. Run the script using a Python interpreter.
2. Enter the file path where you want to store the generated passwords.
3. Enter the desired length for the password.
4. Provide the account name for which you want to generate the password.
5. Choose whether you want to encrypt or decrypt a password.
6. The generated/encrypted password will be written to the specified file.

Note: The encrypted password will be stored in the "GeneratedPasswords.txt" file in the specified directory.

## Example
```
[+]Enter file path (e.g driveLetter:\UserName\UserName\Desktop\Destination): C:\Users\John\Documents
[+]Enter length of password: 10
[+]What is the password for? WebsiteA
```

## Disclaimer
This script provides a basic demonstration of password generation and encryption. Please be aware that it does not cover all aspects of secure password storage and handling. It is recommended to use industry-standard solutions for storing and managing passwords securely.
