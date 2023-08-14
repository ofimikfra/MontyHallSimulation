import random
import os
import pandas as pd
from tabulate import tabulate

def montyHallOriginal():

    num_doors = int(input("\nHow many doors do you want to simulate?\n     -> "))
    doors = list(range(1, num_doors + 1))


    prize_door = random.choice(doors)
    player_choice = #setvalue

    if player_choice == prize_door:
        remaining_door = random.choice([door for door in doors if door != player_choice])

    else:
        remaining_door = prize_door

    switch_choice = #setvalue

    if switch_choice == 'y':
        player_choice = remaining_door

    if_switch = True if switch_choice == "y" else False
    res = "WIN" if player_choice == prize_door else "LOSE"


# ------------------------------------------------------------------------------------------------------------------------------------

def montyHallForget(loop_sim):

    doors = [1,2,3]

    prize_door = random.choice(doors)
    player_choice = #setvalue

    monty_choices = doors.copy()
    if player_choice == prize_door:
        monty_choices.remove(prize_door)
    else:
        monty_choices.remove(player_choice)

    monty_choice = random.choice(monty_choices)

    if monty_choice == prize_door:
        res = "LOSE"

    else:
        switch_choice = #setvalue

        if switch_choice == "y":
            remaining_door = [door for door in doors if door != player_choice and door != monty_choice]
            player_choice = remaining_door[0]

        if_switch = True if switch_choice == "y" else False

        rem_doors = [door for door in doors if door !=monty_choice]

    res = "WIN" if player_choice == prize_door else "LOSE"

# ------------------------------------------------------------------------------------------------------------------------------------

def montyHall2P(loop_sim):

    doors = [1,2,3,4]

    prize_doors = random.sample(doors, 2)
    goat_doors = [door for door in doors if door not in prize_doors]

    player_choice = #setvalue
 
    remaining_doors = doors.copy()
    remaining_doors.remove(player_choice)

    goat_door = random.choice([door for door in remaining_doors if door in goat_doors])
    remaining_doors.remove(goat_door)
        
    switch_choice = #setvalue

    if switch_choice == "y":
        player_choice = random.choice(remaining_doors)
    
    if_switch = True if switch_choice == "y" else False
    res = "WIN" if player_choice in prize_doors else "LOSE"

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