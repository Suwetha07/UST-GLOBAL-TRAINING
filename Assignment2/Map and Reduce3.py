#How would you use the map() function to convert all string elements of a list to uppercase?
fruits=["apple","banana","cherry","mango"]
new_fruits=list(map(lambda x:x.upper(),fruits))
print(new_fruits)
