#Write a List Comprehension to extract all words that are longer than 4 characters from a sentence.
fruits=["banana","kiwi","guva","apple","cherry","mango"]
newfruits=[i  for i in fruits if len(i)>4]
print(list(newfruits))
