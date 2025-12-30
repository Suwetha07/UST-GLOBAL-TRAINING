#Write a program to open a file and handle a FileNotFoundError
f = None
try:
    f = open("ExceptionHandling.py")
    print(f.read())
except FileNotFoundError:
    print("File Doesn't Exist")
else:
    print("File opened Successfully")
finally:
    if f:
        f.close()
