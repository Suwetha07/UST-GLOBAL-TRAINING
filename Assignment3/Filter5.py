#Use filter() to extract all palindromic strings from a list.
txt=["bag","refer","kid","level","radar","sun"]
print(list(filter(lambda x:x[::-1]==x,txt)))
