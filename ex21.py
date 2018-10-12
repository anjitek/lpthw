<<<<<<< HEAD
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(float(input("Please input a float weight:> ")), 2)
inputiq = int(input("Please input an iq value: "))
iq = divide(inputiq, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#print("That becomes: ", what, "Can you do it by hand?")
print(f"That becomes {what} can you do it by mind?")
=======
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(float(input("Please input a float weight:> ")), 2)
inputiq = int(input("Please input an iq value: "))
iq = divide(inputiq, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#print("That becomes: ", what, "Can you do it by hand?")
print(f"That becomes {what} can you do it by mind?")
>>>>>>> d24a6d876ed3850fc689e444bd678b67c7fe3e4d
