#Write a Python program to handle a ZeroDivisionError.

try:
    x=int(input("Enter a value:"))
    z=x/0
except ZeroDivisionError:
     print("Diving by zero is not valid")
else:
    print("Successfully Performed the operation")

finally:
    print("Exception handling is Done Successfully!")
