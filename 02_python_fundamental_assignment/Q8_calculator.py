"""
Assignment: Python Fundamentals - Assignment 02
Question No: Q8
Topic: Functions, Conditions
Author: Aditya Jha
Description:
Simple calculator using function and operation parameter.
"""
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"
    else:
        return "Invalid operation"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

result = calculator(a, b, op)
print("Result:", result)
