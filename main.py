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

WIN = """
YOU PRESSED THE BUTTON TO OPEN THE GATE.
THIS ISN'T THE FIRST TIME YOU"VE DONE THIS.
YOU CAN TIME IT PERFECTLY SO THAT YOU SLIDE THE CAR IN AS THE GATES CLOSE.

YOU KNOW YOU DID THE RIGHT THING.
THE GOVERNMENT WOULD HAVE TORN THE CAR APART,
ANALYSING IT, TESTING IT, THEN DESTROYING IT.

THEY DON'T KNOW ITS SECRETS...
THAT IT HOLDS THE KEY TO DIFFERENT WORLDS.

AS YOU STEP OUT OF THE VEHICLE, JAH RUNS UP TO YOU.
"THANK YOU FOR SAVING ME," HE SAYS.

AS YOU TAKE A COUPLE STEPS AWAY FROM THE CAR,
IT MAKES A STRANGE NOISE.

BEFORE YOUR EYES, IT SHIFTS ITS SHAPE.
YOU'VE SEEN IT BEFORE, BUT ONLY ON TV.

"BUMBLEBEE...?"

"""

LOSE_HUNGER = """
BRUH you just died of hunger LMAO
Should've listened when i told you to eat
Smh good luck next time
"""

LOSE_AGENTS = """
Man they got you, you weren't fast enough
That's tough but sometimes life's just like that
They got you this time, but it's all good
You'll get em next time
"""

LOSE_FUEL = """
Yo what's that sound you're hearing
Did the car get COVID why's it coughing so hard
Oh nvm it's just out of fuel
The agents got u :|
"""

CHOICES = """
    ----
    A. Eat a piece of tofu
    B. Drive at a moderate speed
    C. Speed ahead at full throttle
    D. Stop to refuel (NO FOOD AT GAS STATION)
    E. Status Check
    Q. QUIT
    ----
"""

def type_text_output(string):
    for char in textwrap.dedent(string):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)

def main():
    #type_text_output(INTRODUCTION)

    # CONSTANTS
    MAX_FUEL_LEVEL = 50
    MAX_DISTANCE_TRAVELED = 100
    MAX_TOFU_AMOUNT = 3
    MAX_HUNGER = 50

    # Variables
    done = False
    km_traveled = 0        # 100km is the end
    agents_distance = -20   # 0 is the end
    turns = 0
    tofu = MAX_TOFU_AMOUNT
    fuel = MAX_FUEL_LEVEL
    hunger = 0

    # MAIN LOOP
    while not done:

        # Check if reached END GAME
        # WIN - Travelled the distance required
        if km_traveled > MAX_DISTANCE_TRAVELED:
            time.sleep(2)
            type_text_output(WIN)
            break
        # LOSE - by hunger > MAX_HUNGER (50)
        elif hunger > MAX_HUNGER:
            time.sleep(2)
            type_text_output(LOSE_HUNGER)
            break
        # LOSE - Agents reach you
        elif agents_distance >= 0:
            time.sleep(2)
            type_text_output(LOSE_AGENTS)
            break
        # LOSE - fuel runs out
        elif fuel <= 0:
            time.sleep(2)
            type_text_output(LOSE_FUEL)
            break

        # Random events
        # FIDO - refills your food (5%)
        if tofu < 3 and random.random() < 0.05:
            # refill tofu
            tofu = MAX_TOFU_AMOUNT
            # player feedback
            print("******** You look at your tofu container")
            time.sleep(2)
            print("******** It is filled magically")
            time.sleep(2)
            print("Thanks..... Jah ;)")
            time.sleep(2)

        # DISPLAY HUNGER
        if hunger > 40:
            print("******** You really gotta eat bro.")
            time.sleep(1)
        elif hunger > 25:
            print("******** You're lowwww key hungry")
            time.sleep(1)

        # Present the user their choices
        print(CHOICES)

        user_choice = input("What do you want to do? ").lower().strip("!,.? ")
        if user_choice == "a":
            # EAT/HUNGER
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("-------- That's a nut")
                print("-------- Your hunger is sated")
                print()
            else:
                print()
                print("-------- U literally got no food lmao")
                print()

        elif user_choice == "b":
            # Moderate
            players_distance_now = random.randrange(5, 8)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(2, 5)

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
        else:
            print("\tPlease choose a valid choice.")

        # UPKEEP
        if user_choice in ["b", "c", "d"]:
            hunger += random.randrange(8, 18)
            turns += 1

        time.sleep(1.5)

    # Outro
    print()
    print("Thanks for playing, hopefully I see you again soon")
    print(f"You finished the game in {turns} turns.")

if __name__ == "__main__":
    main()