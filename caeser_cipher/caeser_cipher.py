# Function to prompt user for selection
def get_menu_choice():
    # Print the menu options
    print("*** Menu ***\n")
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit\n")

    # Prompt the user for their choice
    user_selection = int(input("What would you like to do [1,2,3,4]? "))

    # Keep prompting the user until they enter a valid choice
    while user_selection not in range(1, 5):
        user_selection = int(input("Invalid choice, please enter either 1, 2, 3 or 4. "))

    # Return the user's choice
    return user_selection

# Function to encrypt the string
def encrypt_string():
    # Prompt the user for the string to encrypt
    user_string = input("\nPlease enter string to encrypt: ")

    # Get the offset value from the user
    user_offset = get_offset()

    # Initialize the encrypted string
    encrypted_string = ""

    # Iterate over each character in the user's string
    for i in range(0, len(user_string)):
        # Encrypt the character by adding the offset and wrapping around using modulo 128
        # Convert the ASCII value back to a character and append it to the encrypted string
        encrypted_string += chr((ord(user_string[i]) + user_offset) % 128)

    # Print the encrypted string
    print("\nEncrypted string: " + encrypted_string + "\n")

# Function to decrypt the string
def decrypt_string():
    # Prompt the user for the string to decrypt
    user_string = input("\nPlease enter string to decrypt: ")

    # Get the offset value from the user
    user_offset = get_offset()

    # Initialize the decrypted string
    decrypted_string = ""

    # Iterate over each character in the user's string
    for i in range(0, len(user_string)):
        # Decrypt the character by subtracting the offset and wrapping around using modulo 128
        # Convert the ASCII value back to a character and append it to the decrypted string
        decrypted_string += chr((ord(user_string[i]) - user_offset) % 128)

    # Print the decrypted string
    print("\nDecrypted string: " + decrypted_string + "\n")

# Function to brute force decrypt the string
def brute_force_decryption():
    # Prompt the user for the string to decrypt
    user_string = input("Please enter string to decrypt: ")

    # Iterate over all possible offsets from 1 to 94
    for i in range(1, 95):
        # Initialize the decrypted string for this offset
        brute_force_decrypted = ""

        # Iterate over each character in the user's string
        for j in range(0, len(user_string)):
            # Decrypt the character by subtracting the offset
            decrypted_char = ord(user_string[j]) - i
            # If the ASCII value falls below the printable range
            if decrypted_char < 32: 
                # Wrap it around to the end of the printable range
                decrypted_char += 95
            # Convert the ASCII value back to a character and append it to the decrypted string
            brute_force_decrypted += chr(decrypted_char)

        # Print the offset and the decrypted string for this offset
        print("Offset: " + str(i) + ", Decrypted string: " + brute_force_decrypted)
    
    # Print an empty line for better readability
    print("")

# Function to quit the program
def quit():
    # Print a Goodbye message
    print("Goodbye.")

# Function to get the user's offset value
def get_offset():
    # Prompt the user for the offset value
    user_offset = int(input("Please enter offset value (1 to 94): "))

    # Keep prompting the user until they enter a valid offset
    while user_offset not in range(1, 95):
        user_offset = int(input("Invalid choice, please enter an offset value (1 to 94): "))

    # Return the user's offset
    return user_offset

# Main function to run the program
def main():
    # Get the user's menu choice
    user_choice = get_menu_choice()

    # Keep looping until the user chooses to quit
    while user_choice != 4:
        # If the user chose to encrypt a string
        if user_choice == 1:
            encrypt_string()
        # If the user chose to decrypt a string
        elif user_choice == 2:
            decrypt_string()
        # If the user chose to brute force decrypt a string
        elif user_choice == 3:
            brute_force_decryption()
        # Get the user's next menu choice
        user_choice = get_menu_choice()

    # Quit the program
    quit()

if __name__ == "__main__":
    # Call the main function
    main()
