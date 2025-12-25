#Write a Python function that takes a tuple of numbers and returns the sum of all its elements.
def sumofnumber(numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum
numbers=tuple(map(int,input("Enter values :").split()))
print(sumofnumber(numbers))
    
