#Given the tuple t = (1, 2, 3, 4), how can you change the value 3 to 100?
#no tuple cannot change elemets once created  so you can convet to list and then make changes
t = (1, 2, 3, 4)
t=list(t)
t[2:3]=[100]
print(t)

