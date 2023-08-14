import random
import os
import pandas as pd
from tabulate import tabulate

def montyHallNormal(loop_sim):

    wins = 0
    losses = 0
    switches = 0
    win_switch = 0
    lose_switch = 0
    lose_monty = 0

    num_doors = int(input("\nHow many doors do you want to simulate?\n     -> "))
    doors = list(range(1, num_doors + 1))

    i=0
    
    while i < loop_sim:

        prize_door = random.choice(doors)
        player_choice = random.choice(doors)
        init_choice = player_choice

        if player_choice == prize_door:
            remaining_door = random.choice([door for door in doors if door != player_choice])
        else:
            remaining_door = prize_door

        rem_doors = [player_choice, remaining_door]

        yn = ["y", "n"]
        switch_choice = random.choice(yn)
    
        if switch_choice == 'y':
            player_choice = remaining_door

        if_switch = True if switch_choice == "y" else False

        res = "WIN" if player_choice == prize_door else "LOSE"

        simResults(3, i+1, res, if_switch, prize_door, init_choice, rem_doors, player_choice, 0)

        i+=1

    results(sim_results, 1, doors, loop_sim)

# ------------------------------------------------------------------------------------------------------------------------------------

def montyHallForget(loop_sim):

    doors = [1,2,3]

    i=0

    while i < loop_sim:

        prize_door = random.choice(doors)
        player_choice = random.randint(1,3)
        init_choice = player_choice

        monty_choices = doors.copy()
        if player_choice == prize_door:
            monty_choices.remove(prize_door)
        else:
            monty_choices.remove(player_choice)

        monty_choice = random.choice(monty_choices)

        if monty_choice == prize_door:
            res = "LOSE"
            if_switch = "N/A"
            rem_doors = "N/A"

        else:
            yn = ["y", "n"]
            switch_choice = random.choice(yn)

            if switch_choice == "y":
                remaining_door = [door for door in doors if door != player_choice and door != monty_choice]
                player_choice = remaining_door[0]

            if_switch = True if switch_choice == "y" else False

            rem_doors = [door for door in doors if door !=monty_choice]

        res = "WIN" if player_choice == prize_door else "LOSE"

        simResults(2, i+1, res, if_switch, prize_door, init_choice, rem_doors, player_choice, monty_choice)

        i+=1

    results(sim_results, 2, 3, loop_sim)

# ------------------------------------------------------------------------------------------------------------------------------------

def montyHall2P(loop_sim):

    doors = [1,2,3,4]

    i=0

    while i < loop_sim:

        prize_doors = random.sample(doors, 2)
        goat_doors = [door for door in doors if door not in prize_doors]

        player_choice = random.randint(1,4)
        init_choice = player_choice

        remaining_doors = doors.copy()
        remaining_doors.remove(player_choice)
        goat_door = random.choice([door for door in remaining_doors if door in goat_doors])
        remaining_doors.remove(goat_door)

        rem_doors = remaining_doors + [player_choice]
            
        yn = ["y", "n"]
        switch_choice = random.choice(yn)

        if switch_choice == "y":
            player_choice = random.choice(remaining_doors)
        
        if_switch = True if switch_choice == "y" else False

        res = "WIN" if player_choice in prize_doors else "LOSE"

        simResults(3, i+1, res, if_switch, prize_doors, init_choice, rem_doors, player_choice, 0)

        i+=1

    results(sim_results, 3, 4, loop_sim)

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
    mode = int(input("\n(1) Normal Monty Hall     (2) Forgetful Monty Hall     (3) 2 Goats 2 Cars\n     -> "))
    loop = int(input("\nHow many times do you want to play the simulation?\n     -> "))
    if mode == 1:
        montyHallOriginal(loop)
    elif mode == 2:
        montyHallForget(loop)
    elif mode == 3:
        montyHall2P(loop)

modes = {1:"Original Monty Hall", 2:"Forgetful Monty Hall", 3:"2 Prize Monty Hall"}
sim_results = []

def simResults(variation, sim_num, res, if_switch, prize_door, init_choice, rem_doors, final_choice, monty_choice):

    if variation == 1 or variation == 3:
        sim_results.append(
            {
                "Sim No.": sim_num,
                "Result": res,
                "Switched": if_switch,
                "Prize door": prize_door,
                "Initial choice": init_choice,
                "Remaining doors": rem_doors,
                "Final choice": final_choice
            }
        )
    
    if variation == 1:
        print(f"""
SIMULATION RESULTS (Normal Monty Hall variation, {doors_simulated} doors, {loops} simulations):

    if variation == 1 or variation == 3:

        res = {
            "Total wins": wins,
            "Total losses": losses,
            "Number of times switched": switches,
            "Wins due to switching": win_switch,
            "Wins due to not switching": win_not_switch,
            "Losses due to switching": lose_switch,
            "Losses due to not switching": lose_not_switch,
            "Win percentage": f"{winperc}%",
            "Loss percentage": f"{lossperc}%",
            "Winning due to switching": f"{win_switch_perc}%",
            "Winning due to not switching": f"{win_not_switch_perc}%",
            "Losing due to switching": f"{lose_switch_perc}%",
            "Losing due to not switching": f"{lose_not_switch_perc}%"
        }
              
    elif variation == 2:

        lose_monty = len(df_per_sim[df_per_sim["Prize door"] == df_per_sim["Monty's choice"]]) 
        lose_monty_perc = round(((lose_monty / losses) * 100),2)

        res = {
            "Total wins": wins,
            "Total losses": losses,
            "Number of times switched": switches,
            "Wins due to switching": win_switch,
            "Wins due to not switching": win_not_switch,
            "Losses due to switching": lose_switch,
            "Losses due to not switching": lose_not_switch,
            "Losses due to Monty": lose_monty,
            "Win percentage": f"{winperc}%",
            "Loss percentage": f"{lossperc}%",
            "Winning due to switching": f"{win_switch_perc}%",
            "Winning due to not switching": f"{win_not_switch_perc}%",
            "Losing due to switching": f"{lose_switch_perc}%",
            "Losing due to not switching": f"{lose_not_switch_perc}%",
            "Losing due to Monty": f"{lose_monty_perc}%"
        }

    df_per_sim.set_index("Sim No.", inplace=True)
    df_all = pd.DataFrame.from_dict(res, orient='index', columns=["Results"])
    df_all.index.name = "Metrics"
    print(tabulate(df_all, headers="keys", tablefmt="simple"))
    print("\n==============================================================================================================\n")
    print(tabulate(df_per_sim, headers="keys", tablefmt="pretty"))


os.system('clear')
start()

