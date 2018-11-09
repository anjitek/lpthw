<<<<<<< HEAD
=======

>>>>>>> b461db8a2c2a68dba0af42de3df76fd687069fa5
from sys import argv

script, filename = argv

formatter = "{} {} {} {} {} {}" #try using formatter to write

print(f"We're going to erase {filename}.")
print("if you don't want that, hit CTRL-C (^c).")
print("if you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()

print("Now i'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2:")
line3 = input("line 3: ")

print("i' m going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write(formatter.format(line1,"\n",line2,"\n",line3,"\n"))


print("And finally, we close it.")
target.close()
