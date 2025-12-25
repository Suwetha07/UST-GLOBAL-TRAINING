#Write a Python function that merges two dictionaries.
def mergedict(d1,d2):
    d1.update(d2)
    return d1
d1={"a":2,"b":4,"c":6}
d2={"d":8,"e":110,"f":12}
print(mergedict(d1,d2))
