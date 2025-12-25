#Write a program using map() to calculate the length of each word in a list of strings.
names=["alice","david","ronaldo","sam"]
print(list(map(lambda x:len(x),names)))
