#!/usr/bin/env python

import random

def main():
    list1 = [1, 2, 3, 4, 5, 6]
    print("Guess the number!")

    x = random.choice(1, 6)
    guess = None

    while x != guess:

        guess = int(input("Pick a number between 1 - 6: "))

        if x == guess:
            print("You genius!")
        else:
            print("Almost there!")

main()