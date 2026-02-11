# ---------------------------------------------
# Q10: Integer and Fractional Parts
# Problem:
# Take a decimal number as input (e.g., 45.78) and output its:
# - Integer part (45)
# - Fractional part (.78)
# ---------------------------------------------

num = float(input("Enter a decimal number (e.g. 45.78): "))

int_part = int(num)
frac_part = num - int_part

print("Integer part:", int_part)
print("Fractional part:", round(frac_part, 2))
