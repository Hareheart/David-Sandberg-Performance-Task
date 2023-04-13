categories = ["Strength", "Speed", "Durability", "Agility", "Intelligence", "Battle_Iq", "Experience", "Endurance", "Stamina", "Attack_Potency",
              "Knowledge", "Reaction_Speed", "Combat_Speed", "Skill", "Combat", "Versatility", "Scaling","Feats"]

Iron_Man = {
    "Strength": 7,
    "Speed": 8,
    "Durability": 8,
    "Agility": 6,
    "Intelligence": 10,
    "Battle_Iq": 7,
    "Experience": 7,
    "Endurance": 8,
    "Stamina": 6,
    "Attack_Potency": 7,
    "Knowledge": 9,
    "Reaction_Speed": 6,
    "Combat_Speed": 6,
    "Skill": 8,
    "Combat": 6,
    "Versatility": 8,
    "Scaling": 6,
    "Feats": 8,
    "Name": "Iron Man",
}

Spiderman = {
    "Strength": 7,
    "Speed": 6,
    "Durability": 7,
    "Agility": 10,
    "Intelligence": 8,
    "Battle_Iq": 6,
    "Experience": 5,
    "Endurance": 7,
    "Stamina": 6,
    "Attack_Potency": 7,
    "Knowledge": 8,
    "Reaction_Speed": 10,
    "Combat_Speed": 10,
    "Skill": 7,
    "Combat": 6,
    "Versatility": 7,
    "Scaling": 5,
    "Feats": 6,
    "Name": "Spiderman",
}

Hulk = {
    "Strength": 8,
    "Speed": 6,
    "Durability": 9,
    "Agility": 5,
    "Intelligence": 2,
    "Battle_Iq": 2,
    "Experience": 5,
    "Endurance": 9,
    "Stamina": 8,
    "Attack_Potency": 8,
    "Knowledge": 1,
    "Reaction_Speed": 5,
    "Combat_Speed": 8,
    "Skill": 5,
    "Combat": 6,
    "Versatility": 4,
    "Scaling": 7,
    "Feats": 5,
    "Name": "Hulk"
}

Thor = {
    "Strength": 9,
    "Speed": 8,
    "Durability": 10,
    "Agility": 6,
    "Intelligence": 6,
    "Battle_Iq": 10,
    "Experience": 10,
    "Endurance": 10,
    "Stamina": 10,
    "Attack_Potency": 10,
    "Knowledge": 7,
    "Reaction_Speed": 7,
    "Combat_Speed": 6,
    "Skill": 9,
    "Combat": 10,
    "Versatility": 7,
    "Scaling": 10,
    "Feats": 9,
    "Name": "Thor"
}

Captain_Marvel = {
    "Strength": 9,
    "Speed": 9,
    "Durability": 10,
    "Agility": 8,
    "Intelligence": 5,
    "Battle_Iq": 8,
    "Experience": 8,
    "Endurance": 9,
    "Stamina": 8,
    "Attack_Potency": 9,
    "Knowledge": 6,
    "Reaction_Speed": 8,
    "Combat_Speed": 7,
    "Skill": 8,
    "Combat": 9,
    "Versatility": 6,
    "Scaling": 9,
    "Feats": 8,
    "Name": "Captain Marvel"
}

Doctor_Strange = {
    "Strength": 6,
    "Speed": 8,
    "Durability": 6,
    "Agility": 6,
    "Intelligence": 9,
    "Battle_Iq": 9,
    "Experience": 7,
    "Endurance": 6,
    "Stamina": 6,
    "Attack_Potency": 10,
    "Knowledge": 9,
    "Reaction_Speed": 8,
    "Combat_Speed": 7,
    "Skill": 10,
    "Combat": 6,
    "Versatility": 9,
    "Scaling": 9,
    "Feats": 8,
    "Name": "Doctor Strange"
}

Scarlet_Witch = {
    "Strength": 7,
    "Speed": 8,
    "Durability": 7,
    "Agility": 7,
    "Intelligence": 5,
    "Battle_Iq": 6,
    "Experience": 7,
    "Endurance": 7,
    "Stamina": 6,
    "Attack_Potency": 10,
    "Knowledge": 10,
    "Reaction_Speed": 8,
    "Combat_Speed": 6,
    "Skill": 7,
    "Combat": 6,
    "Versatility": 9,
    "Scaling": 9,
    "Feats": 8,
    "Name": "Scarlet Witch"
}

Thanos = {
    "Strength": 9,
    "Speed": 6,
    "Durability": 10,
    "Agility": 5,
    "Intelligence": 9,
    "Battle_Iq": 9,
    "Experience": 10,
    "Endurance": 10,
    "Stamina": 9,
    "Attack_Potency": 10,
    "Knowledge": 9,
    "Reaction_Speed": 9,
    "Combat_Speed": 6,
    "Skill": 10,
    "Combat": 9,
    "Versatility": 9,
    "Scaling": 10,
    "Feats": 10,
    "Name": "Thanos"
}

characters = [Iron_Man, Spiderman, Hulk, Thor, Captain_Marvel, Doctor_Strange, Scarlet_Witch, Thanos]


def main():
    print()
    print("Welcome to the Arena! You will have the chance to pair two MCU characters together in a hypothetical fight and see who ")
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
    game_mode = input("Your available game modes are: 1v1 (1), Battle Royale (2), Make Own Character (3). Which one would you like? ")
    print()

    winner = pair_players(game_mode)
    print("Winner: " + winner)
    print()


def pair_players(game_mode):
    while True:
        if game_mode.lower() == "1v1" or game_mode == "1":
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


        elif game_mode.lower() == "Battle Royale" or game_mode == "2":    
            for character in characters:
                pass
                # if i["Strength"] == 1:
            break

        elif game_mode.lower() == "Make Own Character" or game_mode == "3":
            break

        else:
            print("Your inputted game mode is not one of the avaliable options. Please choose again. ")
            game_mode = input("Your available game modes are: 1v1 (1), Battle Royale (2), Make Own Character (3). Which one would you like? ")


if __name__ == "__main__":
    main()