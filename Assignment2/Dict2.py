#What happens if you try to access a key that does not exist in a dictionary?
dict2={}
n=int(input())
for i in range(n):
    key=input()
    value=input()
    dict2[key]=value
print(dict2)
print(dict2["phone"])

# print(dict2["phone"])
#KeyError: 'phone'
