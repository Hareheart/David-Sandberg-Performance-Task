import random

categories = ["Strength", "Speed", "Durability", "Agility", "Intelligence", "Battle Iq", "Experience", "Endurance", "Stamina", "Attack Potency",
              "Knowledge", "Reaction Speed", "Combat Speed", "Skill", "Combat", "Versatility", "Scaling", "Feats"]

Iron_Man = {
    "Strength": 8,
    "Speed": 8,
    "Durability": 8,
    "Agility": 6,
    "Intelligence": 10,
    "Battle Iq": 7,
    "Experience": 7,
    "Endurance": 8,
    "Stamina": 6,
    "Attack Potency": 7,
    "Knowledge": 9,
    "Reaction Speed": 6,
    "Combat Speed": 6,
    "Skill": 8,
    "Combat": 6,
    "Versatility": 8,
    "Scaling": 6,
    "Feats": 8,
    "Name": "Iron Man",
    "Points": 0
}

Spiderman = {
    "Strength": 7,
    "Speed": 6,
    "Durability": 6,
    "Agility": 10,
    "Intelligence": 8,
    "Battle Iq": 6,
    "Experience": 5,
    "Endurance": 7,
    "Stamina": 6,
    "Attack Potency": 7,
    "Knowledge": 8,
    "Reaction Speed": 10,
    "Combat Speed": 10,
    "Skill": 7,
    "Combat": 6,
    "Versatility": 7,
    "Scaling": 5,
    "Feats": 6,
    "Name": "Spiderman",
    "Points": 0
}

Hulk = {
    "Strength": 9,
    "Speed": 6,
    "Durability": 9,
    "Agility": 5,
    "Intelligence": 2,
    "Battle Iq": 2,
    "Experience": 5,
    "Endurance": 9,
    "Stamina": 8,
    "Attack Potency": 8,
    "Knowledge": 1,
    "Reaction Speed": 5,
    "Combat Speed": 8,
    "Skill": 5,
    "Combat": 6,
    "Versatility": 4,
    "Scaling": 7,
    "Feats": 5,
    "Name": "Hulk",
    "Points": 0
}

Thor = {
    "Strength": 10,
    "Speed": 8,
    "Durability": 10,
    "Agility": 6,
    "Intelligence": 6,
    "Battle Iq": 10,
    "Experience": 10,
    "Endurance": 10,
    "Stamina": 10,
    "Attack Potency": 10,
    "Knowledge": 7,
    "Reaction Speed": 7,
    "Combat Speed": 6,
    "Skill": 9,
    "Combat": 10,
    "Versatility": 7,
    "Scaling": 10,
    "Feats": 9,
    "Name": "Thor",
    "Points": 0
}

Captain_Marvel = {
    "Strength": 10,
    "Speed": 9,
    "Durability": 10,
    "Agility": 8,
    "Intelligence": 5,
    "Battle Iq": 8,
    "Experience": 8,
    "Endurance": 9,
    "Stamina": 8,
    "Attack Potency": 9,
    "Knowledge": 6,
    "Reaction Speed": 8,
    "Combat Speed": 7,
    "Skill": 8,
    "Combat": 9,
    "Versatility": 6,
    "Scaling": 9,
    "Feats": 8,
    "Name": "Captain Marvel",
    "Points": 0
}

Doctor_Strange = {
    "Strength": 6,
    "Speed": 7,
    "Durability": 6,
    "Agility": 6,
    "Intelligence": 9,
    "Battle Iq": 9,
    "Experience": 7,
    "Endurance": 6,
    "Stamina": 6,
    "Attack Potency": 10,
    "Knowledge": 9,
    "Reaction Speed": 8,
    "Combat Speed": 7,
    "Skill": 10,
    "Combat": 6,
    "Versatility": 9,
    "Scaling": 9,
    "Feats": 8,
    "Name": "Doctor Strange",
    "Points": 0
}

Scarlet_Witch = {
    "Strength": 6,
    "Speed": 7,
    "Durability": 7,
    "Agility": 7,
    "Intelligence": 5,
    "Battle Iq": 6,
    "Experience": 6,
    "Endurance": 7,
    "Stamina": 6,
    "Attack Potency": 10,
    "Knowledge": 10,
    "Reaction Speed": 8,
    "Combat Speed": 6,
    "Skill": 7,
    "Combat": 5,
    "Versatility": 9,
    "Scaling": 9,
    "Feats": 8,
    "Name": "Scarlet Witch",
    "Points": 0
}

Thanos = {
    "Strength": 10,
    "Speed": 6,
    "Durability": 10,
    "Agility": 5,
    "Intelligence": 9,
    "Battle Iq": 9,
    "Experience": 10,
    "Endurance": 10,
    "Stamina": 9,
    "Attack Potency": 10,
    "Knowledge": 9,
    "Reaction Speed": 9,
    "Combat Speed": 6,
    "Skill": 10,
    "Combat": 9,
    "Versatility": 9,
    "Scaling": 10,
    "Feats": 10,
    "Name": "Thanos",
    "Points": 0
}

characters = [Iron_Man, Spiderman, Hulk, Thor, Captain_Marvel, Doctor_Strange, Scarlet_Witch, Thanos]


def main():
    print()
    print("Welcome to the Arena! You will have the chance to pair MCU characters together in a hypothetical fight and see who ")
    print("would win depending on a list of 18 different categories determining power level. Your choices include: ")
    print(" 1 - Iron Man")
    print(" 2 - Spiderman")
    print(" 3 - Hulk")
    print(" 4 - Thor")
    print(" 5 - Captain Marvel")
    print(" 6 - Doctor Strange")
    print(" 7 - Scarlet Witch")
    print(" 8 - Thanos")
    print()
    game_mode = input("Your available game modes are: 1v1 (1) and Battle Royale (2). Which one would you like? ")
    print()

    # the winner is returned regardless of the gamemode and printed to the screen
    winner = pair_players(game_mode)
    print("Winner: " + winner)
    print()


def pair_players(game_mode):
    while True:
        if game_mode.lower() == "1v1" or game_mode == "1":
            # only accepts integer that corresponds to character, otherwise, warning and question is given
            while True:
                try:
                    selected_character1 = int(input("Who is the first character you would like to select? Note: Enter the number of the character (ex. Thanos = 8) ")) - 1
                    selected_character2 = int(input("Who is the second character you would like to select? Note: Enter the number of the character (ex. Thanos = 8) ")) - 1
                    break
                except ValueError:
                    print("Please enter an integer representing the character you would like to select. ")

            character1 = characters[selected_character1]
            character2 = characters[selected_character2]

            character1_counter = 0
            character2_counter = 0

            print()
            print("Fight: ", character1["Name"], " VS ", character2["Name"])
            print()

            for category in categories:
                if character1[category] > character2[category]:
                    character1_counter += 1
                    print(category, ":", character1["Name"])
                    print("Score:", character1_counter, ",", character2_counter)
                    print()

                elif character1[category] < character2[category]:
                    character2_counter += 1
                    print(category, ":", character2["Name"])
                    print("Score:", character1_counter, ",", character2_counter)
                    print()

                elif character1[category] == character2[category]:
                    character1_counter += 1
                    character2_counter += 1
                    print(category, ": ", "Both")
                    print("Score: ", character1_counter, ", ", character2_counter)
                    print()
            
            if character1_counter > character2_counter:
                return(character1["Name"])
            elif character1_counter < character2_counter:
                return(character2["Name"])
            elif character1_counter == character2_counter:
                return("Draw")
            
            break

        elif game_mode.lower() == "battle royale" or game_mode == "2":    
            while True:
                try:
                    num_characters = int(input("Please enter the amount of characters you would like to fight: "))
                    print()
                    break
                except ValueError:
                    print("Please enter an integer value.")
                    print()

            selected_characters = []
            for selected_character in range(num_characters):
                # only accepts integer that corresponds to character, otherwise, warning and question is given
                while True:
                    try:
                        selected_character = int(input("Who is the character you would like to select? Note: Enter the number of the character (ex. Thanos = 8) ")) - 1
                        selected_characters.append(characters[selected_character])
                        print()
                        break
                    except ValueError:
                        print("Please enter an integer representing the character you would like to select. ")
                        print()                

            print()
            print("Fighters: ")
            for character in selected_characters:
                print(character["Name"] + ", ", end = "")
            print()
            print()

            # For each category, function is called to determine who gets the points
            for category in categories:
                point = find_point(category, selected_characters)
                print(category, ":", point)
                print()

            winner_count = 0
            winner = None
            for character in selected_characters:
                if character["Points"] > winner_count:
                    winner_count = character["Points"]
                    winner = character["Name"]
                elif character["Points"] == winner_count:
                    winner = winner + " and " + character["Name"]
            
            return(winner)

            break
        
        else:
            print("Your inputted game mode is not one of the avaliable options. Please choose again. ")
            print()
            game_mode = input("Your available game modes are: 1v1 (1) and Battle Royale (2). Which one would you like? ")


def find_point(category, selected_characters):
    max_num = 0
    current = None
    for character in selected_characters:
        if character[category] > max_num:
            max_num = character[category]
            current = character["Name"]
            character["Points"] += 1
        elif character[category] == max_num:
            current = current + " and " + character["Name"]
            character["Points"] += 1
    return current

if __name__ == "__main__":
    main()