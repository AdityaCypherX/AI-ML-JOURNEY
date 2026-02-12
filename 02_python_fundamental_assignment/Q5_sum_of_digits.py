"""
Assignment: Python Fundamentals - Assignment 02
Question No: Q5
Topic: Loops, Modulus Operator
Author: Aditya Jha
Description:
Function to calculate sum of digits of a number.
"""
def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

num = int(input("Enter number: "))
print("Sum of digits:", sum_of_digits(num))
