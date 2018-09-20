print("""You enter a dark room with two doors.
Do you go through door #1 or door #2 ?""")

door = input(">>> ")

if door == "1":
    print("There's a mustang GT5000 and a lamboghini.")
    print("What do you do?")
    print("1. Take GT5000.")
    print("2. Ride lamboghini.")

    bear = input(">> ")

    if bear == "1":
        print("You own a 600 horsepower car. Good job!")
    elif bear == "2":
        print("You owm a 400 thousands pounds car. Well done!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Cars run away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Python.")
    print("2. Java.")
    print("3. C.")

    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of coding.")
        print("Good job!")
    else:
        print("The C powers you in embeded system.")
        print("Good job!")

else:
    print("Don't waste time. Life is going!")
