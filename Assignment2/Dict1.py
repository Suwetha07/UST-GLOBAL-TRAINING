#How can you add a new key-value pair to an existing dictionary in Python?


dict1={}
n=int(input())
for i in  range(n):
    key=input()
    value=input()
    dict1[key]=value
print(dict1)
dict1["Place"]="USA"
print(dict1)
    
