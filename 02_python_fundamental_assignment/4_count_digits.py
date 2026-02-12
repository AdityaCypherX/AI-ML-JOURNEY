"""
Assignment: Python Fundamentals - Assignment 02
Question No: Q4
Topic: Loops
Author: Aditya Jha
Description:
Function to count number of digits in a number.
"""
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

num = int(input("Enter number: "))
print("Total digits:", count_digits(num))
