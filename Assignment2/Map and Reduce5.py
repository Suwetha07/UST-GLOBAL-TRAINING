#Compare and contrast the map() and filter() functions in Python.

#map() function
#map(function, iterable)
#map() applies a function to every element in an iterable and returns the values.

nums = [1,2,3,4]
square = list(map(lambda x: x * 2, nums))
print(square)


##filter() function
#filter(function, iterable)
#filter() selects elements from an iterable based on a condition that is (True / False).
nums = [1, 2, 3, 4 ,5 ,6 ,7 ,8,9,10,11,12]
even_num = list(filter(lambda x: x % 2 == 0, nums))
print(even_num)

