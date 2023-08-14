import random
import os

def montyHallOriginal():

    num_doors = int(input("\nHow many doors do you want to simulate?\n     -> "))
    doors = list(range(1, num_doors + 1))

    print("\n==============================================================================================================")

    prize_door = random.choice(doors)

    while True:
        player_choice = input(f"\nChoose a door between 1 and {num_doors}     -> ")

        if not player_choice.isdigit():
            print(f"\nInvalid choice. Choose a door between 1 and {num_doors}.")
        else:
            player_choice = int(player_choice)
            if player_choice not in doors:
                print(f"\nInvalid choice. Choose a door between 1 and {num_doors}.")
            else:
                break

    if player_choice == prize_door:
        remaining_door = random.choice([door for door in doors if door != player_choice])

    else:
        remaining_door = prize_door

    print(f"\nThe remaining doors are now doors {player_choice} and {remaining_door}.")

    while True:
        switch_choice = input("\nWould you like to switch doors? (y/n)     -> ")

        if switch_choice not in ["y","n"]:
            print("\nInvalid choice. Choose either 'y' or 'n'.")
        else:
            break

    if switch_choice == 'y':
        player_choice = remaining_door
        print(f"\nYou switched to door {player_choice}.")

    if player_choice == prize_door:
        print(f"\nThe prize was in door {prize_door}! You win!")
    else:
        print(f"\nThe prize was in door {prize_door}. You lose :(")


# ------------------------------------------------------------------------------------------------------------------------------------

def montyHallForget():

    doors = [1,2,3]

    prize_door = random.choice(doors)

    print("\n==============================================================================================================")

    while True:
        player_choice = input(f"\nChoose a door between 1 and 3     -> ")

        if not player_choice.isdigit():
            print(f"\nInvalid choice. Choose a door between 1 and 3.")
        else:
            player_choice = int(player_choice)
            if player_choice not in doors:
                print(f"\nInvalid choice. Choose a door between 1 and 3.")
            else:
                break

    monty_choices = doors.copy()
    if player_choice == prize_door:
        monty_choices.remove(prize_door)
    else:
        monty_choices.remove(player_choice)

    monty_choice = random.choice(monty_choices)

    if monty_choice == prize_door:
        print(f"\nMonty revealed door {monty_choice}, and the prize was behind it! You lose :(")

    else:
        while True:
            print(f"\nMonty revealed a door with a goat behind it. The remaining doors are now {[door for door in doors if door != monty_choice]}.")
            switch_choice = input("\nWould you like to switch doors? (y/n)     -> ")

            if switch_choice not in ["y","n"]:
                print("\nInvalid choice. Choose either 'y' or 'n'.")
            else:
                break

        if switch_choice == "y":
            remaining_door = [door for door in doors if door != player_choice and door != monty_choice]
            player_choice = remaining_door[0]

        if player_choice == prize_door:
            print(f"\nThe prize was in door {prize_door}! You win!")
        else:
            print(f"\nThe prize was in door {prize_door}. You lose :(")


# ------------------------------------------------------------------------------------------------------------------------------------

def montyHall2P():

    doors = [1,2,3,4]

    prize_doors = random.sample(doors, 2)
    goat_doors = [door for door in doors if door not in prize_doors]

    print("\n==============================================================================================================")

    while True:
        player_choice = input(f"\nChoose a door between 1 and 4     -> ")

        if not player_choice.isdigit():
            print(f"\nInvalid choice. Choose a door between 1 and 4.")
        else:
            player_choice = int(player_choice)
            if player_choice not in doors:
                print(f"\nInvalid choice. Choose a door between 1 and 4.")
            else:
                break
 
    remaining_doors = doors.copy()
    remaining_doors.remove(player_choice)

    goat_door = random.choice([door for door in remaining_doors if door in goat_doors])
    remaining_doors.remove(goat_door)
        
    while True:
        print(f"\nThe remaining doors are now doors {remaining_doors + [player_choice]}.")
        switch_choice = input("\nWould you like to switch doors? (y/n)     -> ")

        if switch_choice not in ["y","n"]:
            print("\nInvalid choice. Choose either 'y' or 'n'.")
        else:
            break

    while True:
        if switch_choice == "y":
            player_choose = input(f"\nWhich door will you switch to?     -> ")

            if not player_choose.isdigit():
                print(f"\nInvalid choice. Choose a door between 1 and 3.")
            else:
                player_choice = int(player_choose)
                if player_choice not in remaining_doors:
                    print(f"\nInvalid choice. Choose a door between 1 and 3.")
                else:
                    break
    
    if player_choice in prize_doors:
        print(f"\nThe prize was in door {player_choice}! You win!")
    else:
        print(f"\nThe prize was in doors {prize_doors}. You lose :(")

# ------------------------------------------------------------------------------------------------------------------------------------

def start():
    print("""

███╗   ███╗ ██████╗ ███╗   ██╗████████╗██╗   ██╗    ██╗  ██╗ █████╗ ██╗     ██╗     
████╗ ████║██╔═══██╗████╗  ██║╚══██╔══╝╚██╗ ██╔╝    ██║  ██║██╔══██╗██║     ██║     
██╔████╔██║██║   ██║██╔██╗ ██║   ██║    ╚████╔╝     ███████║███████║██║     ██║     
██║╚██╔╝██║██║   ██║██║╚██╗██║   ██║     ╚██╔╝      ██╔══██║██╔══██║██║     ██║     
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║   ██║      ██║       ██║  ██║██║  ██║███████╗███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝      ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝

███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗            
██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗           
███████╗██║██╔████╔██║██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝           
╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗           
███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║           
╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝        

==============================================================================================================
    """)

    print("Welcome to the Monty Hall Simulator! Select the variation:")
    mode = int(input("\n(1) Original Monty Hall     (2) Forgetful Monty Hall     (3) 2 Prize Monty Hall\n     -> "))
    if mode == 1:
        montyHallOriginal()
    elif mode == 2:
        montyHallForget()
    elif mode == 3:
        montyHall2P()

os.system('clear')
start()