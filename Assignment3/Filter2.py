#Write a program using filter() to select all words from a list that start with a vowel
fruits=["apple","mango","orange","avacado","dates"]
print(list(filter(lambda x:x[0]=="a" or x[0]=="e"or x[0]=="i" or x[0]=="o" or x[0]=="u",fruits)))
