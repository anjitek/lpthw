<<<<<<< HEAD
=======

>>>>>>> b461db8a2c2a68dba0af42de3df76fd687069fa5
from sys import argv

script, user_name, version = argv
prompt = '>>>>>> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Hello, dear sir {user_name}, i m Ai {version}.
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
