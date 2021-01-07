# main.py
# Midnight Rider
# A text-based adventure game.
# Gamespot gives it 9 out of 10.

import random
import sys
import textwrap
import time


INTRODUCTION = """
WELCOME TO MIDNIGHT RIDER

WE"VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THAT"S WHY THE GOVERNMENT WANTS IT.

WE CAN'T LET THEM HAVE IT

ONE GOAL: SURVIVAL... and THE CAR
REACH THE END BEFORE THE MAN GON GET U.

------
"""

CHOICES =   """
    ----
    B. Drive at a moderate speed
    C. Speed ahead at full throttle
    D. Stop to refuel (NO FOOD AT GAS STATION)
    E. Status Check
    Q. QUIT
    ----
"""

def intro():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)

def main():
    #intro()

    # CONSTANTS
    MAX_FUEL_LEVEL = 50

    # Variables
    done = False
    km_traveled = 0        # 100km is the end
    agents_distance = -20   # 0 is the end
    turns = 0
    tofu = 3                # 3 is max
    fuel = MAX_FUEL_LEVEL
    hunger = 0

    # MAIN LOOP
    while not done:
        # TODO: Check if reached END GAME

        # TODO: Present the user their choices
        print(CHOICES)

        user_choice = input("What do you want to do? ").lower().strip("!,.? ")
        if user_choice == "b":
            # Moderate
            players_distance_now = random.randrange(7, 15)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(3, 7)

            # Player distance traveled
            km_traveled += players_distance_now

            # Agents distance traveled
            agents_distance -= players_distance_now - agents_distance_now

            # Feedback to player
            print()
            print("nice nice")
            time.sleep(0.5)
            print(f"-------- You traveled {players_distance_now} kilometers")
        elif user_choice == "c":
            pass
            # FAST
            players_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(5, 11)

            # Player distance traveled
            km_traveled += players_distance_now

            # Agents distance traveled
            agents_distance -= players_distance_now - agents_distance_now

            # Feedback to player
            print()
            print("YEET")
            time.sleep(0.5)
            print(f"-------- You traveled {players_distance_now} kilometers")
        elif user_choice == "d":
            # Fill up the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give player feedback
            print()
            print("-------- You filled the fuel tank.")
            print("-------- The agents got closer...")
            print()
        elif user_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkm traveled: {km_traveled}")
            print(f"\tFuel remaining: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms behind")
            print(f"\tYou have {tofu} tofu left")
            print(f"\t--------\n")
        elif user_choice == "q":
            print("Thanks for playing g you a real one :)")
            done = True

        time.sleep(1.5)

        # TODO: Change the environment based on
        #       user choice, and RNG
        # TODO: Random event generator


if __name__ == "__main__":
    main()