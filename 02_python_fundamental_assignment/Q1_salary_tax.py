"""
Assignment: Python Fundamentals - Assignment 02
Question No: Q1
Topic: Conditional Statements
Author: Aditya Jha

Description:
Program to calculate tax rate based on salary slabs.
"""
salary = float(input("Enter your salary: "))

if salary < 30000:
    tax_rate = 5
elif 30000 <= salary <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

print(f"Final Tax Rate: {tax_rate}%")
