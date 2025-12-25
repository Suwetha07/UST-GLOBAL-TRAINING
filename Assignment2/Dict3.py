#Write a Python function that takes a dictionary and returns a list of keys that have values greater than 50.
def greater(dict3):
    result=[]
    for key,value in dict3.items():
        if value > 50:
           result.append(key)
    return result
dict3={}
n=int(input())
for i in range(n):
   key=input()
   value=int(input())
   dict3[key]=value
print(greater(dict3))
