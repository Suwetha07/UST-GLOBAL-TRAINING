#What is the difference between a list and a tuple in Python?
#list are mutable and tuple are immutable
lst=list(map(int,input("Enter values for list:").split()))
lst.insert(1,5)
print(lst)

tuple3=tuple(map(int,input("Enter value for tuple:").split()))
tuple3.insert(1,5)
print(tuple3)

# tuple3.insert(1,5)
#AttributeError: 'tuple' object has no attribute 'insert
