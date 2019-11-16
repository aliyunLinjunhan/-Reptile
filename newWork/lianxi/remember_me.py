import json

filename = "username.json"
try:
    with open(filename) as fp:
        name = json.load(fp)
except FileNotFoundError:
    name = input("What is your name?")
    with open(filename, 'w') as fp:
        json.dump(name, fp)
        print("We will remember you when you come back "+ name + "!")
else:
    print("Welcome back " + name + "!")