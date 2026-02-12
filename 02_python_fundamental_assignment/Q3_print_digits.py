"""
Assignment: Python Fundamentals - Assignment 02
Question No: Q3
Topic: Loops, Modulus Operator
Author: Aditya Jha
Description:
Program to print all digits of a number.
"""
n = int(input("Enter number: "))
while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10
