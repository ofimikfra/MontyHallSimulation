import random
import time
import os

def montyHallNormal(loop_sim):

    wins = 0
    losses = 0
    switches = 0
    win_switch = 0
    lose_switch = 0
    lose_monty = 0

    num_doors = int(input("\nHow many doors do you want to simulate?\n    -> "))
    doors = set(range(1, num_doors + 1))

    print("\n--------------------------------------------------------------------------------\n")

    print(f"In this simulator, there are {num_doors} doors.")
    time.sleep(1.5)
    print("Behind one of the doors, there is a car. Behind the rest of the doors are goats.")
    time.sleep(1.5)
    print("You must pick a door that you think the car is behind.")
    time.sleep(1.5)
    print("Then, Monty will reveal all of the doors with goats, and leave 2 doors unopened.")
    time.sleep(1.5)
    print("You can choose whether to switch to the unopened door or stick with the one you chose.")
    time.sleep(1.5)
    print("Good luck!")
    time.sleep(1.5)

    i=0
    
    while i < loop_sim:

        prize_door = random.randint(1, num_doors)

        print("\n--------------------------------------------------------------------------------\n")
        
        print(f"SIMULATION NO. {i+1}\n")

        #DEBUGGING
        #print(f"\nThere is a car behind door {prize_door}.")

        player_choice = int(input(f"\nChoose a door between 1-{num_doors}: "))

        while player_choice not in doors:
            player_choice = input("Invalid choice. Choose a door between 1-3: ")

        print(f"\nYou chose door {player_choice}.")
        time.sleep(1)

        # determine remaining door
        if player_choice == prize_door:
            # if chosen door has prize, remaining door is random door that is not prize door
            remaining_door = random.choice(list(doors - {player_choice}))
        else:
            # if chosen door does not have prize, remaining door is door with the prize
            remaining_door = prize_door

        print(f"\nAll doors except door {player_choice} and door {remaining_door} were revealed to have goats behind them.")
        time.sleep(1.5)

        # player decides to switch/stick door
        switch_choice = input(f"\nDo you want to switch to door {remaining_door}? (y/n): ")
        while switch_choice not in ["y", "n"]:
            switch_choice = input("Invalid choice. Choose again (y/n): ").lower()
        if switch_choice.lower() == 'y':
            player_choice = remaining_door
            print(f"\nYou switched to door {remaining_door}...")
            switches+=1
            time.sleep(2)
        else:
            print(f"\nYou stuck with door {player_choice}...")
            time.sleep(2)

        if player_choice == prize_door:
            print(f"\nCongratulations, the car was behind door {prize_door}!\n")
            wins+=1
        else:
            print(f"\nSorry, the car was behind door {prize_door}. You switched to door {player_choice}. Better luck next time!\n")
            losses+=1

        #results calculator
        if switch_choice.lower() == "y" and player_choice == prize_door:
            win_switch+=1
        elif switch_choice.lower() == "y" and player_choice != prize_door:
            lose_switch+=1

        time.sleep(1.5)
        i+=1

    results(loop_sim, 1, num_doors, wins, losses, switches, win_switch, lose_switch, lose_monty)

# ------------------------------------------------------------------------------------------------------------------------------------

def montyHallForget(loop_sim):

    wins = 0
    losses = 0
    switches = 0
    win_switch = 0
    lose_switch = 0
    lose_monty = 0

    #set doors & car
    doors = [1,2,3]
    
    print("\n--------------------------------------------------------------------------------\n")
    
    # Ask the player to choose a door
    print(f"In this simulator, there are 3 doors.")
    time.sleep(1.5)
    print("Behind one of the doors, there is a car. Behind the rest of the doors are goats.")
    time.sleep(1.5)
    print("You must pick a door that you think the car is behind.")
    time.sleep(1.5)
    print("Then, monty will reveal all of the doors with goats, and leave 2 doors unopened.")
    time.sleep(1.5)
    print("You can choose whether to switch to the unopened door or stick with the one you chose.")
    time.sleep(1.5)
    print("In this version of Monty Hall, Monty doesn't know where the car is either.")
    time.sleep(1.5)
    print("There's a chance that Monty reveals the door with the car behind it, so choose wisely!")
    time.sleep(1.5)
    print("Good luck!")
    time.sleep(1.5)

    i=0

    while i < loop_sim:

        prize_door = random.choice(doors)

        print("\n--------------------------------------------------------------------------------\n")
        
        print(f"SIMULATION NO. {i+1}\n")

        #DEBUGGING
        #print(f"\nThere is a car behind door {prize_door}.")

        player_choice = int(input("\nChoose a door between 1-3: "))

        while player_choice not in doors:
            player_choice = int(input("Invalid choice. Choose a door between 1-3: "))

        print(f"\nYou chose door {player_choice}.")
        time.sleep(1)

        # Monty chooses a door that doesn't have the prize and isn't the player's choice
        monty_choices = doors.copy()
        if player_choice == prize_door:
            monty_choices.remove(prize_door)
        else:
            monty_choices.remove(player_choice)

        monty_choice = random.choice(monty_choices)

        if monty_choice == prize_door:
            monty_result = f"\nThe car was behind door {monty_choice}! Better luck next time!"
            lose_monty+=1
            losses+=1
        else:
            monty_result = f"\nThere was a goat behind door {monty_choice}!"

        print(f"\nMonty opens door {monty_choice}...")
        time.sleep(1.5)
        print(monty_result)

        if monty_choice != prize_door:
            # Ask the player if they want to switch or stick with their initial choice
            switch_choice = input("\nDo you want to switch to the other unopened door? (y/n): ").lower()
            while switch_choice not in ["y", "n"]:
                switch_choice = input("Invalid choice. Choose again (y/n): ").lower()
            if switch_choice == "y":
                remaining_doors = [door for door in doors if door != player_choice and door != monty_choice]
                player_choice = remaining_doors[0]
                print(f"\nYou switched to door {player_choice}...")
                switches+=1
                time.sleep(1)
            else:
                print(f"\nYou stuck with door {player_choice}...")
                time.sleep(1)

            # Check if the player's final choice is the winning door and display the result
            if player_choice == prize_door:
                print(f"\nCongratulations! The car was behind door {prize_door}!\n")
                wins+=1
            else:
                print(f"\nSorry, the car was behind door {prize_door}. Better luck next time!\n")
                losses+=1

            #results calculator
            if switch_choice.lower() == "y" and player_choice == prize_door:
                win_switch+=1
            elif switch_choice.lower() == "y" and player_choice != prize_door:
                lose_switch+=1

        time.sleep(1.5)
        i+=1

    results(loop_sim, 2, 3, wins, losses, switches, win_switch, lose_switch, lose_monty)

# ------------------------------------------------------------------------------------------------------------------------------------

def montyHall22(loop_sim):

    wins = 0
    losses = 0
    switches = 0
    win_switch = 0
    lose_switch = 0
    lose_monty = 0

    # Set up the doors and prizes
    doors = [1, 2, 3, 4]

    print("\n--------------------------------------------------------------------------------\n")

    # Ask the player to choose a door
    print(f"In this simulator, there are 4 doors.")
    time.sleep(1.5)
    print("Behind two of these four doors is a car, and behind the other two doors are goats.")
    time.sleep(1.5)
    print("You must pick a door that you think a car is behind.")
    time.sleep(1.5)
    print("Then, Monty will reveal a door with a goat behind it, and leave 3 doors unopened.")
    time.sleep(1.5)
    print("You can choose whether to switch to one of the unopened doors or stick with the one you chose.")
    time.sleep(1.5)
    print("Good luck!")
    time.sleep(1.5)

    i=0

    while i < loop_sim:

        car_doors = random.sample(doors, 2)
        goat_doors = [door for door in doors if door not in car_doors]

        print("\n--------------------------------------------------------------------------------\n")

        print(f"SIMULATION NO. {i+1}\n")

        # FOR DEBUGGING:
        # print(f"\nThere is a car behind door {car_doors[0]} and {car_doors[1]}.")

        player_choice = int(input("\nChoose a door from 1-4: "))

        while player_choice not in doors:
            player_choice = int(input("Invalid choice. Choose a door from 1-4: "))

        print(f"\nYou chose door {player_choice}.")
        time.sleep(1)

        # Reveal one of the goat doors that the player didn't choose
        remaining_doors = doors.copy()
        remaining_doors.remove(player_choice)
        goat_door = random.choice([door for door in remaining_doors if door in goat_doors])
        remaining_doors.remove(goat_door)
        print(f"\nMonty reveals that door {goat_door} has a goat behind it.")
        time.sleep(1.5)

        # Ask the player if they want to switch doors
        switch_choice = input("\nDo you want to switch to another door? (y/n): ").lower()

        # Make sure the player's choice is valid
        while switch_choice not in ["y", "n"]:
            switch_choice = input("Invalid choice. Choose again (y/n): ").lower()

        # If the player chooses to switch, pick the remaining unopened door
        if switch_choice == "y":
            print(f"\nThe remaining doors are:")
            print(remaining_doors)
            new_choice = int(input("Which door would you like to switch to?\n   -> "))

            while new_choice not in [door for door in doors if door not in [player_choice, goat_door]]:
                new_choice = int(input("Invalid choice. Which door would you like to switch to?\n   -> "))
            
            player_choice = new_choice
            switches+=1

            print(f"\nYou switched to door {player_choice}...")
            time.sleep(1)

        else:
            print(f"\nYou stick with door {player_choice}...")
            time.sleep(1)

        # Determine if the player won or lost
        if player_choice in car_doors:
            print(f"\nCongratulations! There was a car was behind door {player_choice}!\n")
            wins+=1
        else:
            print(f"\nSorry, the cars were behind door {car_doors[0]} and door {car_doors[1]}. Better luck next time!\n")
            losses+=1

        #results calculator
        if switch_choice.lower() == "y" and player_choice in car_doors:
            win_switch+=1
        elif switch_choice.lower() == "y" and player_choice not in car_doors:
            lose_switch+=1

        time.sleep(1.5)
        i+=1

    results(loop_sim, 3, 4, wins, losses, switches, win_switch, lose_switch, lose_monty)

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

--------------------------------------------------------------------------------
    """)

    print("Welcome to the Monty Hall Simulator! Select the variation:")
    mode = int(input("\n(1) Normal Monty Hall     (2) Forgetful Monty Hall     (3) 2 Goats 2 Cars\n     -> "))
    loop = int(input("\nHow many times do you want to play the simulation?\n     -> "))
    if mode == 1:
        montyHallNormal(loop)
    elif mode == 2:
        montyHallForget(loop)
    elif mode == 3:
        montyHall22(loop)

def results(loops, variation, doors_simulated, wins, losses, switches, win_switch, lose_switch, lose_monty):
    print("\n--------------------------------------------------------------------------------\n")
    if variation == 1:
        print(f"""
SIMULATION RESULTS (Normal Monty Hall variation, {doors_simulated} doors, {loops} simulations):

Total wins: {wins}
Total losses: {losses}
Number of times switched: {switches}
Wins due to switching: {win_switch}
Losses due to switching: {lose_switch}

Win percentage: {round((wins/loops)*100,2)}%
Lose percentage: {round((losses/loops)*100,2)}%
Probability of winning due to switching: {round((win_switch/switches)*100,2)}%
Probability of losing due to switching: {round((lose_switch/switches)*100,2)}%""")
              
    elif variation == 2:
        print(f"""
SIMULATION RESULTS (Forgetful Monty Hall variation, {doors_simulated} doors, {loops} simulations):

Total wins: {wins}
Total losses: {losses}
Number of times switched: {switches}
Wins due to switching: {win_switch}
Losses due to switching: {lose_switch}
Losses due to Monty: {lose_monty}

Win percentage: {round((wins/loops)*100,2)}%
Lose percentage: {round((losses/loops)*100,2)}%
Probability of winning due to switching: {round((win_switch/switches)*100,2)}%
Probability of losing due to switching: {round((lose_switch/switches)*100,2)}%
Probability of losing due to Monty: {round((lose_monty/loops)*100,2)}%""")

    elif variation == 3:
        print(f"""
SIMULATION RESULTS (Monty Hall with 2 goats & 2 doors variation, {doors_simulated} doors, {loops} simulations):

Total wins: {wins}
Total losses: {losses}
Number of times switched: {switches}
Wins due to switching: {win_switch}
Losses due to switching: {lose_switch}

Win percentage: {round((wins/loops)*100,2)}%
Lose percentage: {round((losses/loops)*100,2)}%
Probability of winning due to switching: {round((win_switch/switches)*100,2)}%
Probability of losing due to switching: {round((lose_switch/switches)*100,2)}%""")

    print("\n--------------------------------------------------------------------------------")

os.system('clear')
start()

