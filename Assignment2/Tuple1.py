#Ccan you modify the elements of a tuple after it has been created? Why or why not?


#No, Tuple is immutbale .once tuple is created we cannot modify them.
tuple1=tuple(map(int,input("Enter values:").split()))
tuple1.append(9)
print(tuple1)

#error
# tuple1.append(9)
#AttributeError: 'tuple' object has no attribute 'append'
