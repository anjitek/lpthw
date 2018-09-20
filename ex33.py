i = 0
numbers = []
"""
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
"""

j = int(input("Input a number: "))
numgap = int(input("input a increasing gap: "))

# for i in range(0, j, numgap):
while i < j:
    print(f"At the top i is {i}")
    numbers.append(i)
    i = i + numgap
    print(f"number gaaaaaaap is : {numgap}")
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
