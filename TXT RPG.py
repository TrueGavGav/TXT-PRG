import os

def newgame():
    newgame_choice = input("1. New game\n2. Quit\nAnswer 1 or 2: ")
    if newgame_choice == '1':
        print("New game started")
    elif newgame_choice == '2':
        os._exit(0)

def name():
    name = input("Mysterious Voice:\nWhy Hello My Wonderful Specimen, Now What Would Your Name Be? ")
    print("Mysterious Voice:\nAh, so you are called " + name + ". What a wonderful name!")
    print("Now, you will be sent to a wide and not so wonderful world!")

def introduction():
    print("\nYou wake up in a silent city, the once bustling streets now deserted.")
    print("Buildings loom over you like silent sentinels, their windows empty and dark.")
    print("The only sound is the rustle of leaves in the wind, and the distant echo of your own footsteps.")

# Player stats here ->
HP = 10
ATT = 10
SPE = 10

newgame()
name()
introduction()
