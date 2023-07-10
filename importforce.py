#echo force.0 

#import packages
import hashlib

def convert_to_integer():
    # Read the 5-character string from the user
    user_input = input("Enter a 5-character string: ")

    # Convert the string to bytes and hash using SHA-256
    hashed_bytes = hashlib.sha256(user_input.encode()).digest()

    # Convert the hashed bytes to an integer
    hashed_integer = int.from_bytes(hashed_bytes, byteorder='big')

    # Add "!" at the beginning and "$" at the end of the integer
    result = "!" + str(hashed_integer) + "$"

    # Return the final result
    return result
