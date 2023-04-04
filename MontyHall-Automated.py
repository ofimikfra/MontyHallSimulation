import random
import os

def montyHallNormal(loop_sim):

    wins = 0
    losses = 0
    switches = 0
    win_switch = 0
    lose_switch = 0
    lose_monty = 0

    num_doors = int(input("\nHow many doors do you want to simulate?\n     -> "))
    doors = set(range(1, num_doors + 1))

    i=0
    
    while i < loop_sim:

        prize_door = random.randint(1, num_doors)
        player_choice = random.randint(1,num_doors)

        #DEBUGGING
        #old_player_choice = player_choice

        # determine remaining door
        if player_choice == prize_door:
            # if chosen door has prize, remaining door is random door that is not prize door
            remaining_door = random.choice(list(doors - {player_choice}))
        else:
            # if chosen door does not have prize, remaining door is door with the prize
            remaining_door = prize_door

        #switch/stick door
        yn = ["y", "n"]
        switch_choice = random.choice(yn)
    
        if switch_choice == 'y':
            player_choice = remaining_door
            switches+=1

        if player_choice == prize_door:
            wins+=1
            #DEBUGGING
            #print("\nwin")
        else:
            #DEBUGGING
            #print("\nlose")
            losses+=1

        #results calculator
        if switch_choice == "y" and player_choice == prize_door:
            win_switch+=1
        elif switch_choice == "y" and player_choice != prize_door:
            lose_switch+=1

        #DEBUGGING
        #print(f"""
        #Doors: {num_doors}
        #Prize door: {prize_door}
        #Player choice: {old_player_choice}
        #Remaining door: {remaining_door}""")
        #if switch_choice == "y":
        #    print(f"""
        #    Switch choice: {switch_choice}
        #    Player choice (new): {player_choice}""")

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

    doors = [1,2,3]

    i=0

    while i < loop_sim:

        prize_door = random.choice(doors)
        player_choice = random.randint(1,3)

        #DEBUGGING
        #old_player_choice = player_choice

        # Monty chooses a door that doesn't have the prize and isn't the player's choice
        monty_choices = doors.copy()
        if player_choice == prize_door:
            monty_choices.remove(prize_door)
        else:
            monty_choices.remove(player_choice)

        monty_choice = random.choice(monty_choices)

        if monty_choice == prize_door:
            lose_monty+=1
            losses+=1
            #DEBUGGING
            #print("\nlose")

        else:
            # Ask the player if they want to switch or stick with their initial choice
            yn = ["y", "n"]
            switch_choice = random.choice(yn)
            if switch_choice == "y":
                remaining_doors = [door for door in doors if door != player_choice and door != monty_choice]
                player_choice = remaining_doors[0]
                switches+=1

            # Check if the player's final choice is the winning door and display the result
            if player_choice == prize_door:
                #DEBUGGING
                #print("\nwin")
                wins+=1
            else:
                #DEBUGGING
                #print("\nlose")
                losses+=1

            #results calculator
            if switch_choice.lower() == "y" and player_choice == prize_door:
                win_switch+=1
            elif switch_choice.lower() == "y" and player_choice != prize_door:
                lose_switch+=1

        #DEBUGGING
        #print(f"""
        #Doors: {doors}
        #Prize door: {prize_door}
        #Player choice: {old_player_choice}
        #Monty's door choices: {monty_choices}
        #Monty's choice: {monty_choice}""")
        #if monty_choice != prize_door:
        #    print(f"""
        #    Switch choice: {switch_choice}""")
        #    if switch_choice == "y":
        #        print(f"""
        #    Remaining doors: {remaining_doors}
        #    Player choice (new): {player_choice}""")

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

    doors = [1, 2, 3, 4]

    i=0

    while i < loop_sim:

        car_doors = random.sample(doors, 2)
        goat_doors = [door for door in doors if door not in car_doors]

        player_choice = random.randint(1,4)

        #DEBUGGING
        #old_player_choice = player_choice

        #Reveal one of the goat doors that the player didn't choose
        remaining_doors = doors.copy()
        remaining_doors.remove(player_choice)
        goat_door = random.choice([door for door in remaining_doors if door in goat_doors])
        remaining_doors.remove(goat_door)
            
        #Ask the player if they want to switch doors
        yn = ["y", "n"]
        switch_choice = random.choice(yn)

        if switch_choice == "y":
            new_choice = random.choice(remaining_doors)
            player_choice = new_choice
            switches+=1

        # Determine if the player won or lost
        if player_choice in car_doors:
            wins+=1
            #DEBUGGING
            #print("\nwin")
        else:
            losses+=1
            #DEBUGGING
            #print("\nlose")

        #results calculator
        if switch_choice.lower() == "y" and player_choice in car_doors:
            win_switch+=1
        elif switch_choice.lower() == "y" and player_choice not in car_doors:
            lose_switch+=1

        #DEBUGGING
        #print(f"""
        #Car doors: {car_doors}
        #Goat doors: {goat_doors}
        #Player choice: {old_player_choice}
        #Goat door: {goat_door}
        #Remaining doors: {remaining_doors}
        #Switch choice: {switch_choice}""")
        #if switch_choice == "y":
        #    print(f"""
        #    New choice: {new_choice}
        #    Player choice (new): {player_choice}""")

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

