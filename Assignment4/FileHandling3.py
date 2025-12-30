#Write a Python program to count the number of lines, words, and characters in a text file.
f = open("filehandling.txt", "r")
count_lines = 0
count_words = 0
count_chars = 0

for line in f:
    count_lines += 1
    count_chars += len(line)
    words = line.split()
    count_words += len(words)
f.close()
print("Number of lines:", count_lines)
print("Number of words:", count_words)
print("Number of characters:", count_chars)
