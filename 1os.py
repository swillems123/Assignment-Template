import os
import random
import string
import time

def random_password_generator(length=12, include_lowercase=True, include_uppercase=True, include_numbers=True, include_punctuation=True, exclude_chars=""):
    """
    Generate a random password based on specified criteria.

    Parameters:
    - length (int): Length of the password.
    - include_lowercase (bool): Whether to include lowercase characters.
    - include_uppercase (bool): Whether to include uppercase characters.
    - include_numbers (bool): Whether to include numeric characters.
    - include_punctuation (bool): Whether to include punctuation symbols.
    - exclude_chars (str): A string of characters to exclude from the password.

    Returns:
    - str: The generated password.
    """
    # Define character sets
    char_set = ""
    if include_lowercase:
        char_set += string.ascii_lowercase
    if include_uppercase:
        char_set += string.ascii_uppercase
    if include_numbers:
        char_set += string.digits
    if include_punctuation:
        char_set += string.punctuation

    # Exclude specified characters
    char_set = ''.join(c for c in char_set if c not in exclude_chars)

    if not char_set:
        raise ValueError("No characters available to generate the password. Check your options.")

    # Generate password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def memorable_password_generator(num_words=3, case="lower", word_list_file=r"C:\\Users\\sethw\\Documents\\GitHub\\Assignmet-Template\\top_english_nouns_lower_100000.txt"):
    """
    Generate a memorable password using random words and numbers.

    Parameters:
    - num_words (int): Number of words in the password.
    - case (str): Case for the words ("lower", "upper", or "capitalize").
    - word_list_file (str): Path to the file containing the word list.

    Returns:
    - str: The generated password.
    """
    # Load word list
    try:
        with open(word_list_file, "r") as file:
            words = [line.strip() for line in file]
    except FileNotFoundError:
        raise FileNotFoundError(f"Word list file '{word_list_file}' not found.")

    # Select random words
    selected_words = random.sample(words, num_words)

    # Adjust case
    if case == "upper":
        selected_words = [word.upper() for word in selected_words]
    elif case == "capitalize":
        selected_words = [word.capitalize() for word in selected_words]

    # Append random digits and concatenate with hyphen
    memorable_password = "-".join(f"{word}{random.randint(0, 9)}" for word in selected_words)
    return memorable_password

def save_password(password, password_type):
    """
    Save the generated password with a timestamp to the appropriate file.

    Parameters:
    - password (str): The generated password.
    - password_type (str): Either 'Random' or 'Memorable'.
    """
    # Define directory and file paths
    directory = password_type
    file_path = os.path.join(directory, "Generated_Passwords.txt")

    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Log the password with a timestamp
    with open(file_path, "a") as file:
        timestamp = time.strftime("%H:%M:%S")
        file.write(f"{timestamp} - {password}\n")

if __name__ == "__main__":
    # Ask user for input on password type
    print("Password Generator")
    password_type = input("Choose password type (memorable/random): ").strip().lower()

    if password_type == "memorable":
        try:
            num_words = int(input("Enter the number of words (e.g., 3): "))
        except ValueError:
            print("Invalid input. Using default of 3 words.")
            num_words = 3

        case = input("Choose word case (lower/upper/capitalize): ").strip().lower()
        if case not in ["lower", "upper", "capitalize"]:
            print("Invalid case input. Using default 'lower'.")
            case = "lower"

        # Generate memorable password
        password = memorable_password_generator(num_words=num_words, case=case)
        print(f"Generated Memorable Password: {password}")

        # Save password
        save_password(password, "Memorable")

    elif password_type == "random":
        try:
            length = int(input("Enter the password length (e.g., 12): "))
        except ValueError:
            print("Invalid input. Using default length of 12.")
            length = 12

        include_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == "yes"
        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        include_punctuation = input("Include punctuation symbols? (yes/no): ").strip().lower() == "yes"
        exclude_chars = input("Enter characters to exclude (leave blank for none): ").strip()

        # Generate random password
        try:
            password = random_password_generator(
                length, 
                include_lowercase, 
                include_uppercase, 
                include_numbers, 
                include_punctuation, 
                exclude_chars
            )
            print(f"Generated Random Password: {password}")

            # Save password
            save_password(password, "Random")
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("Invalid password type. Please choose either 'memorable' or 'random'.")

