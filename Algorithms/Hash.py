import hashlib
import os

def password_to_binary(password):
    """Converts password characters to their binary representations."""
    binary_password = ""
    for char in password:
        binary_char = bin(ord(char))[2:]
        binary_password += binary_char + " "
    return binary_password.strip()

def binary_value(binary_string):
    """Converts binary strings back to decimal values."""
    binary_list = binary_string.split()
    decimal_values = []
    for binary_num in binary_list:
        decimal_value = int(binary_num, 2)
        decimal_values.append(decimal_value)
    return decimal_values

def concatenate_numbers(numbers):
    """Concatenates a list of numbers into a single string."""
    concatenated = ""
    for number in numbers:
        concatenated += str(number)
    return concatenated

def modulo_result(concatenated_number, divisor):
    """Calculates the modulo result of a concatenated number."""
    result = int(concatenated_number) % divisor
    return result

def hash_password(password, salt=None):
    """Hashes the password using PBKDF2 with SHA-256."""
    if salt is None:
        salt = os.urandom(16)  # generating random salt
    else:
        salt = salt.encode('utf-8')

    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt.hex() + hashed_password.hex()

def sha256_hash(data):
    """Calculates the SHA-256 hash of the given data."""
    sha256_hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return sha256_hash

password = input("Enter password: ")
salt = input("Enter salt: ")

hashed_password = hash_password(password, salt)
print("Hashed password:", hashed_password)

binary_password = password_to_binary(hashed_password)
print("Password in binary system:", binary_password)

decimal_values = binary_value(binary_password)
print("Binary values converted to decimal:", decimal_values)

concatenated_number = concatenate_numbers(decimal_values)
print("Concatenated numbers:", concatenated_number)

divisor = int(input("Enter divisor: "))
mod_result = modulo_result(concatenated_number, divisor)
print("Modulo result:", mod_result)

hashed_result = sha256_hash(concatenated_number)
print("Hashed result using sha function:", hashed_result)
