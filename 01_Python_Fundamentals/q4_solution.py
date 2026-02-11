# ---------------------------------------------
# Q4: Type Conversion
# Problem:
# The user enters a string containing a number (e.g., "45").
# Convert it to:
# - an integer
# - a float
# - a string again
# Print all three values with their types.
# ---------------------------------------------

#when the input is pure numeric
number=input("enter the string ")
if number.isdigit():
  num1=int(number)
  num2=float(number)
  num3=str(number)
  
  print(" integer number is:",num1)
  print(" float number is:",num2)
  print(" string number is:",num3)
else:
  print("input is not a pure number")



#when string contain a number(like abc123...)
number=input("enter the string")
digits=''.join(char for char in number if char.isdigit())
if digits:
  num1=int(digits)
  num2=float(digits)
  num3=str(digits)

  print("integre num is:",num1)
  print("float num is:",num2)
  print("string num is:",num3)
else:
  print("no number found in the string")
