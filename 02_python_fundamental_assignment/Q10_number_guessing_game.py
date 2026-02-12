"""
Assignment: Python Fundamentals - Assignment 02
Question No: Q10
Topic: Loops, Conditions
Author: Aditya Jha
Description:
Number guessing game program.
"""

secret_number = 7
while True:
    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break
