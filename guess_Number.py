#!/usr/bin/env python3
"""
Simple Python example - Number guessing game
"""

import random

def guessing_game():
    """A simple number guessing game"""
    number = random.randint(1, 10)
    attempts = 0
    
    print("Welcome! I'm thinking of a number between 1 and 10.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You got it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    guessing_game()