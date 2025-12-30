#Write a program to copy the contents of one text file into another file.
f=open("filehandling.txt")
copy=f.read()
f.seek(0)
c=open("filehandlingcopy.txt","w")
c.write(copy)
f.close()
c.close()
