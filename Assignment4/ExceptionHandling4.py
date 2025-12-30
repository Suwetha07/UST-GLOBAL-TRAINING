try:
    mylist=[1,2,3,4,5]
    print(mylist[4])
except IndexError:
    print("Invalid Index")
except TypeError:
    print("Invalid operation")
except:
    print("Index value must be integer")
else:
    print("Sucessfully fetched the index value")
finally:
    print("List accessing done")
