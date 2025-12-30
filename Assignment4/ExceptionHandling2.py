#Write a program that accepts user input and handles a ValueError if the input is not an integer.

try:
    n=int(input("Enter a integer value:"))
    print("You have  entered Integer")
except ValueError:
    print("Please enter integer")
else:
    print("You have executed try block")
