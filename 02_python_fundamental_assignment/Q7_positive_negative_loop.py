"""
Assignment: Python Fundamentals - Assignment 02
Question No: Q7
Topic: While Loop, Conditions
Author: Aditya Jha
Description:
Program to continuously check positive/negative until user enters 'Quit'.
"""
while True:
    user_input = input("Enter a number or type 'Quit': ")

    if user_input.lower() == "quit":
        print("Program terminated.")
        break

    num = float(user_input)

    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
