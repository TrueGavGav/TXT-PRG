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

def action():
    action = input("What Do You Do?\n1. Nothing\n2. Walk Around\n3. Check Inventory\n")
    if action == "1":
        print("You decide to do nothing.")
        callaction()
    elif action == "2":
        print("You decide to walk around.")
        callaction()
    elif action == "3":
        open_inventory()
    else:
        print("Invalid input.")
        callaction()

def callaction():
    action()

def open_inventory():
    print("Inventory:")
    print("1. " + inv_item1)
    print("2. " + inv_item2)
    print("3. " + inv_item3)
    print("4. " + inv_item4)
    print("5. " + inv_item5)
    inv_action = input("Choose An Item: ")
    if inv_action == "1":
        inv_action2 = input("Do What With This Item?\n1. Use\n2. Throw Away\n")
        if inv_action2 == "1":
            print("You used " + inv_item1)
            action()
        elif inv_action2 == "2":
            print("You threw away " + inv_item1)
            action()
        else:
            print("Invalid input.")
            open_inventory()
    elif inv_action == "2":
        inv_action2 = input("Do What With This Item?\n1. Use\n2. Throw Away\n")
        if inv_action2 == "1":
            print("You used " + inv_item2)
            action()
        elif inv_action2 == "2":
            print("You threw away " + inv_item2)
            action()
        else:
            print("Invalid input.")
            open_inventory()
    elif inv_action == "3":
        inv_action2 = input("Do What With This Item?\n1. Use\n2. Throw Away\n")
        if inv_action2 == "1":
            print("You used " + inv_item3)
            action()
        elif inv_action2 == "2":
            print("You threw away " + inv_item3)
            action()
        else:
            print("Invalid input.")
            open_inventory()
    elif inv_action == "4":
        inv_action2 = input("Do What With This Item?\n1. Use\n2. Throw Away\n")
        if inv_action2 == "1":
            print("You used " + inv_item4)
            action()
        elif inv_action2 == "2":
            print("You threw away " + inv_item4)
            action()
        else:
            print("Invalid input.")
            open_inventory()
    elif inv_action == "5":
        inv_action2 = input("Do What With This Item?\n1. Use\n2. Throw Away\n")
        if inv_action2 == "1":
            print("You used " + inv_item5)
            action()
        elif inv_action2 == "2":
            print("You threw away " + inv_item5)
            action()
        else:
            print("Invalid input.")
            open_inventory()

# Player stats here ->
HP = 10
ATT = 10
SPE = 10
LV = 1
EXP = 10
EXP_TO_NEXT_LEVEL = EXP * 2 / 1.25

# Inventory items here ->
inv_item1 = "Health Potion"
inv_item2 = "Bandages"
inv_item3 = "Food Rations"
inv_item4 = "Flashlight"
inv_item5 = "Knife"

newgame()
name()
introduction()
action()
