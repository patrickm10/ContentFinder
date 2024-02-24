"""
Learning how to encrypt and decrypt files
"""
import base64
import pandas as pd


def get_data(username):
    """
    Function to get metadata from instagram
    :param username: username of the user
    :return: dictionary of metadata
    """

def show_encryption_path(password):
    """
    Takes in a hashed password and shows what was done to the password to get the hashed password
    :param password: hashed password
    :return: DataFrame of the steps to get the hashed password
    """
    print(f"Encrypted Password: {password}")
    path = []
    path.append("Hashed_pwd")
    steps_data = []
    for i in range(len(password)):
        step = f"Step {i+1}: {password[i]} -> {ord(password[i])} -> {chr(ord(password[i]))}"
        path.append(step)
        steps_data.append({"Step": f"Character {i+1}", "Character": password[i], "ASCII": ord(password[i]), "Decoded Character": chr(ord(password[i]))})
    steps_df = pd.DataFrame(steps_data)
    steps_df = steps_df.set_index("Step")
    steps_df = steps_df.reindex(columns=["Character", "ASCII", "Decoded Character"])
    print(steps_df)

def decode_pwd(pwd):
    """
    Function to help the pwd
    :param password: encrypted pwd
    :return: decrypted pwd
    """
    pwd = base64.b64decode(pwd)
    pwd = pwd.decode('utf-8')
    return pwd

def encode_password(password):
    """
    Function to encrypt the password
    :param password: password to be encrypted
    :return: encrypted password
    """
    password = password.encode('utf-8')
    # Creates a hashed password with b64 encoding
    password = base64.b64encode(password)
    # Creates a hashed password with a85 encoding
    # password = base64.a85encode(password)
    return password


def word_guesser(pwd: str):
    """
    Character by character search algorithm to guess a word
    :param pwd: str - The word to guess
    :return: str
    Time Complexity O(n)
    """
    
    # Decode the password
    password = decode_pwd(pwd)
    
    # Get the length of the word
    password_length = len(password)

    # Initialize an empty string to store the guessed characters
    guessed_chars_str = ""
    count = 0

    # Iterate over each position of the word
    for position in range(1, password_length + 1):
        # Initialize a flag to indicate whether the character is found
        char_found = False

        # Iterate over each possible lowercase letter, number, and special character
        for char in range(ord('a'), ord('z') + 1):
            # Perform your search operation here
            # You can replace the print statement with your desired search logic
            print(f"Character in position_{position}: {chr(char)}")
            count += 1

            # Check if the guessed character matches the character at the current position in the word
            if chr(char) == password[position - 1]:
                # If the guess is correct, append it to the guessed characters string
                guessed_chars_str += chr(char)
                char_found = True
                print(f"Position {position} Character: {chr(char)}\n")
                if guessed_chars_str == pwd:
                    return guessed_chars_str
                else:
                    print(f"Guessed word so far: {guessed_chars_str}\n")
                    break
        
        # If no lowercase character is found, return None
        for char in range(ord('A'), ord('Z') + 1):
                # print(f"Character in position_{position}: {chr(char)}")
                count += 1

                if chr(char) == password[position - 1]:
                    guessed_chars_str += chr(char)
                    char_found = True
                    print(f"Position {position} Character: {chr(char)}\n")
                    if guessed_chars_str == password:
                        return guessed_chars_str
                    else:
                        print(f"Guessed word so far: {guessed_chars_str}\n")
                        break
                    
        # TODO: Add a check for special characters
        
        # TODO: Add binary search to find faster
        # If no lowercase character is found, iterate over each possible digit and special character
        if not char_found:
            for char in range(ord('0'), ord('9') + 1):
                # For it to look cooler
                # print(f"Character in position_{position}: {chr(char)}")
                count += 1

                if chr(char) == password[position - 1]:
                    guessed_chars_str += chr(char)
                    char_found = True
                    print(f"Position {position} Character: {chr(char)}\n")
                    if guessed_chars_str == password:
                        print(f"Original Password: {pwd}")
                        print(f"Password Unlocked: {guessed_chars_str} in {count} attempts.")
                        return guessed_chars_str
                    else:
                        print(f"Guessed word so far: {guessed_chars_str}\n")
                        break

        # If no character is found, return None
        if not char_found:
            print("Word not guessed")
            return None

    # Otherwise, return the guessed characters string
    # return guessed_chars_str


def main():
    """
    Main function
    """
    print("------------------Testing to encrypt_password function------------------\n")
    password = "Watch me figure this out!"
    print(f"Password: {password}")
    print(f"Encrypted Pwd: {password}\n")
    print("------------------Testing to decode function------------------")
    # decoded_pwd = decode_pwd(password)
    # print(f"Decrypted Pwd: {decoded_pwd}\n")
    print("------------------Testing to show_encryption_path function------------------")
    print(show_encryption_path(password))
    print("------------------Testing to word_guesser function------------------")
    word = "wAtchthis10"
    # Encrypt the password
    word = encode_password(word)
    print(f"Encrypted Password: {word}")
    word_guesser(word)
    print("------------------Testing to compare_algorithms function------------------\n")
    

main()