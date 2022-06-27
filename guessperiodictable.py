#!/usr/bin/env python

import random

def main():
    """Start a periodic table guessing game."""
    print("Guess the element!")

    Periodic = [
        "Hydrogen",
        "Lithium",
        "Sodium",
        "Potassium",
        "Rubidium",
        "Cesium",
        "Francium"
        ]

    x = random.choice(Periodic)
    guess = None

    while x != guess:

        guess = str(input("I stand at the most left side of periodic table. Which element am I? "))
        
        if x == guess:
            print("Oh wow, a chemist has been born!")
        else:
            print("Really, kid? Think again.")

main()