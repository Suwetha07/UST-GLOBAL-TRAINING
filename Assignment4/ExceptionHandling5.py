#Write a program to handle multiple exceptions in a single try block.
dict1 = {'a': 1, 'b': 2}

try:
    y = dict1['a'] + dict1['c']
    print(y)
except KeyError as e:
    print("Missing key:", e)
except TypeError as e:
    print("Type mismatch:", e)
except Exception as e:
    print("Other error:", e)
