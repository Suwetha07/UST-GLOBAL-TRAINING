#How would you iterate over both keys and values of a dictionary in Python?
dict4={}
n=int(input())
for i in range(n):
      key=input()
      value=input()
      dict4[key]=value
for key ,value in dict4.items():
      print(key,value)
