"""
Assignment: Python Fundamentals - Assignment 02
Question No: Q9
Topic: Loops, Conditions
Author: Aditya Jha
Description:
Function to check whether a number is prime or not.
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")
