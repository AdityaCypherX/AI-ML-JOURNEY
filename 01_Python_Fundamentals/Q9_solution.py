# ---------------------------------------------
# Q9: Simple Interest
# Problem:
# Ask the user for:
# Principal (P), Rate (R), Time (T).
# Convert all to float and compute simple interest.
#
# Formula:
# SI = (P * R * T) / 100
# ---------------------------------------------
P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate (R): "))
T = float(input("Enter Time (T): "))

SI = (P * R * T) / 100
print("Simple Interest:", SI)
