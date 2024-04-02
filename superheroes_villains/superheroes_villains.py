# Function to read characters.txt file that stores character data
def read_file(filename):
    # Open the file in read mode
    with open(filename, "r") as file:
        # Initialise an empty list to store characters
        character_list = []  
        # Initialise an empty sublist to store individual character details
        sublist = []
        # Enumerate over each line in the file
        for index, line in enumerate(file):
            # Remove leading and trailing whitespaces from the line
            line = line.strip()
            # If the line is not empty, append it to the sublist
            if line != "":
                sublist.append(line)
            # After every 3 lines (which constitute one character's details), append the sublist to the main list
            if (index + 1) % 3 == 0: 
                character_list.append(sublist)
                 # Reset the sublist for the next character
                sublist = []
        # If there are any remaining lines in the sublist after reading the entire file, append them to the main list
        if sublist:  
            character_list.append(sublist)
    # Return the list of characters
    return character_list

# Function to write the character data to a file
def write_to_file(filename, character_list):
    # Open the file in write mode
    with open(filename, "w") as file:
        # Iterate over each character in the character list
        for line in character_list:
            # Iterate over each detail of a character
            for item in line:
                # Write the detail to the file
                file.write(item)
                # Write a newline character after each detail
                file.write("\n")

# Function to display characters based on the display type
def display_characters(character_list, display_type):
    # Print the header for the character summary
    print("\n===================================================")
    print("-     Character (heroes and villains) Summary     -")
    print("===================================================")  
    print("-                             P  W  L  D  Health  -")
    print("---------------------------------------------------")  
    # Iterate over each character in the character list
    for character in character_list:
        # Extract the statics for battles played, battles won, battles lost, and draws for each character
        stats = character[2][1:].strip().split()
        # If the display type is 0 (uses "list" command), print all characters
        if display_type == 0:
            print(f"- {character[0]:<25} {stats[0]:>3} {stats[1]:>2} {stats[2]:>2} {stats[3]:>2} {stats[4]:>7}  -")
            print("---------------------------------------------------")  
        # If the display type is 1 (uses "heroes" command), print only heroes
        elif display_type == 1:
            if "h" in character[2]:
                print(f"- {character[0]:<25} {stats[0]:>3} {stats[1]:>2} {stats[2]:>2} {stats[3]:>2} {stats[4]:>7}  -")
                print("---------------------------------------------------")  
        # If the display type is 2 (uses "villains" command), print only villains
        elif display_type == 2:
            if "v" in character[2]:
                print(f"- {character[0]:<25} {stats[0]:>3} {stats[1]:>2} {stats[2]:>2} {stats[3]:>2} {stats[4]:>7}  -")
                print("---------------------------------------------------")  
    # Print the footer for the character summary
    print("===================================================\n")
    # Return the last character processed
    return character

# Function to find a character in the character list
def find_character(character_list, name):
    # Iterate over each character in the character list
    for index in range(len(character_list)):
        # If the character's name matches the given name
        if name == character_list[index][0]:
            # Return the index of the character and the name
            return index, name
    # Return -1 and the name if the character is not found
    return -1, name

# Function to search for a character in the character list and return statistics
def search(character_list, name):
    # Use index to find the character
    index, name = find_character(character_list, name)
    # If the character is found, print hero if "h" found or villain if "v" found. Else, print not found
    if index != -1:
        if "h" in character_list[index][2]:
            print("\nAll about " + name + " --> HERO")
        elif "v" in character_list[index][2]:
            print("\nAll about " + name + " --> VILLAIN")
        # Initialise stats and print all the information about the character
        stats = character_list[index][2][1:].split()
        print("\nSecret identity: " + character_list[index][1])
        print("\nBattles fought: " + stats[0])
        print(" > No Won:    " + stats[1])
        print(" > No Lost:   " + stats[2])
        print(" > No Drawn:  " + stats[3])
        print("\nCurrent health: " + stats[4] + "%")
    else:
        print("\n" + name + " is not found in character (heroes and villains) list.")

# Function to find character and reset health to 100
def reset(character_list, name):
    # Split the character's stats into a list
    index, name = find_character(character_list, name)
    if index != -1:
        stats = character_list[index][2].split()
        # Reset the character's health to 100
        stats[5] = '100'
        # Join the stats back into a string and assign it back to the character
        character_list[index][2] = ' '.join(stats)
        print("\nSuccessfully updated " + name + "'s health to 100")
    else:
        print("\n" + name + " is not found in character (heroes and villains) list.")

# Function to add a new character to the character list
def add_character(character_list, name, secret_identity, hero):
    index, _ = find_character(character_list, name)
    if index == -1:
        # If the character does not exist, create a new character with the given details
        new_character = [name, secret_identity, hero + ' 0 0 0 0 100']
        # Add the new character to the character list
        character_list.append(new_character)
        print("\nSuccessfully added " + name + " to character list.")
        # Write the updated character list to the file
        write_to_file("new_characters.txt", character_list)
    else:
        print(" \n" + name + " already exists in character list.")
    # Return the updated character list
    return character_list

# Function to remove a character from the character list
def remove_character(character_list, name):
    # Use the find_character function to find the character in the list
    index, name = find_character(character_list, name)
    # If the character is found, remove it from the list
    if index != -1:
        del character_list[index]
        print("\nSuccessfully removed " + name + " from character list.")
    # Return the updated character list
    return character_list

# Function to display the character with the highest number of battles won
def display_highest_battles_won(character_list):
    # Initialise the highest number of battles won and the lowest number of battles played
    highest_battle_won = 0
    lowest_battle_played = float('inf')
    best_character = None
    # Iterate over each character in the character list
    for character in character_list:
        # Extract the character's battle data
        character_data = character[2].split(" ")
        battles_won = int(character_data[2])
        battles_played = int(character_data[1])
        # If the character has won more battles than the current best, or has won the same number of battles but played fewer, update the best character
        if battles_won > highest_battle_won or (battles_won == highest_battle_won and battles_played < lowest_battle_played):
            highest_battle_won = battles_won
            lowest_battle_played = battles_played
            best_character = character
    # If no character has won a battle, return an error message
    if highest_battle_won == 0:
        return "\nError: No character has won a battle."
    else:
        # Print the character with the highest number of battles won
        print("\nHighest number of battles won => " + best_character[0] + " with " + str(highest_battle_won) + " opponents defeated!")
    # Return the best character
    return best_character

def update_statistics(character, play, win, loss, draw):
    # Find the character in the list
    hero = character[2][0]
    stats = character[2][1:].strip().split()
    # Update the play, win, loss, and draw stats
    stats[0] = str(int(stats[0]) + play)
    stats[1] = str(int(stats[1]) + win)
    stats[2] = str(int(stats[2]) + loss)
    stats[3] = str(int(stats[3]) + draw)
    # Join the stats back into a string and update the character's stats
    character[2] = hero + ' ' + ' '.join(stats)

def update_health(character, damage):
    # Extract the character's current health from the character data
    health = int(character[2][1:].strip().split()[4])
    # Calculate the character's health after taking the damage
    current_health = max(health - damage, 0)
    # Update the character's health in the character data
    character[2] = character[2].replace(str(health), str(current_health))
    # Return the character's current health
    return current_health

def do_battle(character_list, opponent1_pos, opponent2_pos):
    # Importing the random module for generating random numbers
    import random
    # Initialise variables for winner and loser
    winner = ""
    loser = ""
    # Ask the user for the number of battle rounds and ensure it's between 1 and 5
    battle_rounds = int(input("\nPlease enter number of battle rounds: "))
    while battle_rounds not in range(1, 6):
        print("Must be between 1-5 inclusive.")
        battle_rounds = int(input("\nPlease enter number of battle rounds: "))  
    # Print the battle start message
    print("\n-- Battle --")
    print("\n" + character_list[opponent1_pos][0] + " versus " + character_list[opponent2_pos][0] + " - " + str(battle_rounds) + " rounds")
    # Initialise the health of the opponents
    health1 = update_health(character_list[opponent1_pos], 0)
    health2 = update_health(character_list[opponent2_pos], 0)
    # Initialise the number of completed rounds
    rounds_completed = 0
    # Start the battle rounds
    while rounds_completed < battle_rounds and (health1 != 0 and health2 != 0):
        # Increment the number of completed rounds
        rounds_completed += 1
        # Generate random damage for each opponent
        damage1 = random.randint(0, 50)
        damage2 = random.randint(0, 50)
        # Update the health of the opponents after taking damage
        health1 = update_health(character_list[opponent1_pos], damage1)
        health2 = update_health(character_list[opponent2_pos], damage2)
        # Print the round details
        print("\nRound: " + str(rounds_completed))
        print(" > " + character_list[opponent1_pos][0] + " - Damage: " + str(damage1) + " - Current health: " + str(health1))
        print(" > " + character_list[opponent2_pos][0] + " - Damage: " + str(damage2) + " - Current health: " + str(health2))
    # Print the end of battle message
    print("\n-- End of battle --")
    # Compare the health of the two opponents to determine the winner and loser
    # If opponent1 has more health, they are the winner
    if health1 > health2:
        winner = opponent1_pos
        loser = opponent2_pos
    # If opponent2 has more health, they are the winner
    elif health1 < health2:
        winner = opponent2_pos 
        loser = opponent1_pos
    # If both opponents have the same health, it's a tie
    elif health1 == health2:
        winner = None 

    # Check if the battle ended in a tie
    if winner is None:
        # Print a message indicating a tie
        print("\n-- A tie. Nobody wins!")
        # Update the statistics for both opponents to reflect the tie
        update_statistics(character_list[opponent1_pos], 1, 0, 0, 1)
        update_statistics(character_list[opponent2_pos], 1, 0, 0, 1)
    else:
        # If there's a winner, print a message indicating the loser has died
        print("\n-- " + character_list[loser][0] + " has died! :(")
        # Print a message indicating the winner
        print("\n** " + character_list[winner][0] + " wins! **")
        # Update the statistics for the winner to reflect the win
        update_statistics(character_list[winner], 1, 1, 0, 0)
        # Update the statistics for the loser to reflect the loss
        update_statistics(character_list[loser], 1, 0, 1, 0)

# Function to sort a list of characters by health and number of battles
def sort_by_health(character_list):
    # Create a copy of the character list to avoid modifying the original list
    sorted_list = character_list.copy()
    # Implement bubble sort to sort the characters
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list) - i - 1):
            # Extract the health of the current character and the next character
            health_j = int(sorted_list[j][2][1:].split()[4])
            health_j1 = int(sorted_list[j + 1][2][1:].split()[4])
            # If the current character has less health than the next character, swap them
            if health_j < health_j1:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
            # If the current character and the next character have the same health
            elif health_j == health_j1:
                # Extract the number of battles of the current character and the next character
                battles_j = int(sorted_list[j][2][1:].split()[0])
                battles_j1 = int(sorted_list[j + 1][2][1:].split()[0])
                # If the current character has less battles than the next character, swap them
                if battles_j < battles_j1:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    # Return the sorted list of characters
    return sorted_list

# Function to interact with the user and perform various operations on the character list
def interactive_mode(character_list):
    # Define the valid commands
    commands = ["list", "heroes", "villains", "search", "reset", "add", "remove", "high", "battle", "health", "quit"]
    # Ask the user to enter a command
    user_command = input("\nPlease enter choice\n[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ")
    # Continue to interact with the user until they enter "quit"
    while user_command != "quit":
        # If the user's command is not valid, print an error message
        if user_command not in commands:
            print("\nNot a valid command. Please try again.\n")
        else:
            # If the user's command is "list", display all characters
            if user_command == "list":
                display_characters(character_list, 0)
            # If the user's command is "heroes", display all heroes
            elif user_command == "heroes":
                display_characters(character_list, 1)
            # If the user's command is "villains", display all villains
            elif user_command == "villains":
                display_characters(character_list, 2)
            # If the user's command is "search", find the character via search() function
            elif user_command == "search":
                name = input("\nPlease enter name: ")
                search(character_list, name)
            # If the user's command is "reset", ask for a character's name and reset the character
            elif user_command == "reset":
                name = input("\nPlease enter name: ")
                reset(character_list, name)
            # If the user's command is "add", ask for the character's details and add the character
            elif user_command == "add":
                name = input("\nPlease enter name: ")
                secret_identity = input("Please enter secret_identity: ")
                hero = input("Is this character a hero or villain [h|v]? ")
                add_character(character_list, name, secret_identity, hero)
            # If the user's command is "remove", ask for a character's name and remove the character
            elif user_command == "remove":
                name = input("\nPlease enter name: ")
                remove_character(character_list, name)
            # If the user's command is "high", display the character with the highest battles won
            elif user_command == "high":
                display_highest_battles_won(character_list)
            # If the user's command is "battle", ask for the names of two opponents and simulate a battle between them
            elif user_command == "battle":
                # Use valid_input as a flag to check if the user's input is valid
                valid_input = False
                # Validation for opponent 1
                while not valid_input:
                    name1 = input("\nPlease enter opponent one's name: ")
                    opponent1_pos, _ = find_character(character_list, name1)
                    if opponent1_pos == -1:
                        print(name1 + " is not found in the character list - please enter another opponent!")
                    else:
                        valid_input = True
                valid_input = False
                # Validation for opponent 2
                while not valid_input:
                    name2 = input("Please enter opponent two's name: ")
                    if name2 == name1:
                        print(name2 + " cannot battle themself.")
                    else:
                        opponent2_pos, _ = find_character(character_list, name2)
                        if opponent2_pos == -1:
                            print(name2 + " is not found in the character list - please enter another opponent!")
                        else:
                            valid_input = True
                # Once two opponents chosen, call do_battle function
                do_battle(character_list, opponent1_pos, opponent2_pos)
            # If the user's command is "health", sort the characters by health and display them
            elif user_command == "health":
                sorted_list = sort_by_health(character_list)
                display_characters(sorted_list, 0)
        # Ask the user to enter a command for the next iteration
        user_command = input("\nPlease enter choice\n[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ")
    # Print a termination message and write the character list to a file
    print("\n-- Program Terminating! --\n")
    write_to_file("new_characters.txt", character_list)
    # Return the last command entered by the user
    return user_command

# Main function to run the program
def main():
    # Initialise an empty list to store the characters
    character_list = []
    # Initialise filename as characters.txt
    filename = "characters.txt"
    # Read the characters from the file and store them in the list
    character_list = read_file(filename)
    # Call the interactive mode function
    interactive_mode(character_list)

# If this file is the main file being run, run the main function
if __name__ == "__main__":
    main()