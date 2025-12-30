word = input("Enter word to search: ")
f = open("filehandling.txt", "r")
line_no = 1
found = False
for line in f:
    if word in line:
        print("Word found at line:", line_no)
        found = True
    line_no += 1

if not found:
    print("Word not found")

f.close()
