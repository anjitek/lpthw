<<<<<<< HEAD
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) #read from the start

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

#try rewind function
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
=======
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) #read from the start

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

#try rewind function
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
>>>>>>> d24a6d876ed3850fc689e444bd678b67c7fe3e4d
