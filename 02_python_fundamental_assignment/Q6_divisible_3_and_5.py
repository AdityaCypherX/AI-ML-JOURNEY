"""
Assignment: Python Fundamentals - Assignment 02
Question No: Q6
Topic: Loops, Conditions
Author: Aditya Jha
Description:
Program to print numbers from 1 to 100 divisible by both 3 and 5.
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
