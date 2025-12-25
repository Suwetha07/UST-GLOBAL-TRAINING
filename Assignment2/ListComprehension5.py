#Can you use an if condition inside a list comprehension? Provide an example where only odd numbers are selected from a list.
x=[8,3,1,6,9,4,7]
odd= [ i  for i in x  if i%2!=0]
print(list(odd))
