# ---------------------------------------------
# Q6: Swapping Two Numbers
# Problem:
# Write a program to swap the values of two numbers
# entered by the user.
# ---------------------------------------------
# Q6: Swap two numbers( Without Temp Variable (Pythonic Way – Tuple Unpacking)
n1 = input("Enter first number: ")
n2 = input("Enter second number: ")

n1, n2 = n2, n1
print("After swapping:")
print("First number:", n1)
print("Second number:", n2)
print("-" * 50)



#Using a Temp Variable (Traditional Method)
n1 = input("Enter first number: ")
n2 = input("Enter second number: ")

temp = n1
n1 = n2
n2 = temp

print("After swapping:")
print("First number:", n1)
print("Second number:", n2)
print("-" * 50)

#Without Temp (Using + and -) (numeric only)
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2

print("After swapping:")
print("First number:", n1)
print("Second number:", n2)
print("-" * 50)
