<<<<<<< HEAD
#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Albert", "Shelly")
print_two_again("Miko", "Morning")
print_one("Rita")
print_none()
=======
#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Albert", "Shelly")
print_two_again("Miko", "Morning")
print_one("Rita")
print_none()
>>>>>>> d24a6d876ed3850fc689e444bd678b67c7fe3e4d
