#How does the map() function work in Python? Give an example where you square each number in a list.
# map takes two arguments map(function,iterable) .A function that applies to each item in a iterable ,that returns map object.
numbers=[1,2,3,4,5,6]
print(list(map(lambda x:x*x,numbers)))
