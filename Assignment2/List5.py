#Write a Python function that removes duplicates from a list without using the set() function.

def duplicate(numbers):
    newlist=[]
    for num in numbers:
        if num not in newlist:
            newlist.append(num)
    return newlist
numbers=list(map(int,input("Enter values :").split()))
print(duplicate(numbers))
