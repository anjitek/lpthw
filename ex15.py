
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename} (by agrv):")
print(txt.read())
txt.close()

print("Type the filename again:(by input)", end = ' ')
#intended (end = ' ') at the end, makes input in the same line.
file_again = input(">>>> ")
txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
