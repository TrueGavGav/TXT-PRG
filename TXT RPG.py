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
  action = input("What Do You Do?\n1.Nothing\n2.Walk Around\n3.Check Inventory")
  if action == "1":
    open_inventory()


def open_inventory():
  inventory = print("1." + inv_item1 + "2." + inv_item2 + "3." + inv_item3 + "4." + inv_item4 + "5." + inv_item5 +)
  inv_action = input("Choose An Item")
  if inv_action = "1":
    inv_action2 = input("Do What With This Item?\n1.Use\n2.Throw Away")
    if inv_action2 == "1":
      print("")
      elif inv_action2 == "2":
        print("")

  elif inv_action = "2":
    inv_action2 = input("Do What With This Item?\n1.Use\n2.Throw Away")
    if inv_action2 == "1":
      print("")
      elif inv_action2 == "2":
        print("")

  elif inv_action = "3":
    inv_action2 = input("Do What With This Item?\n1.Use\n2.Throw Away")
    if inv_action2 == "1":
      print("")
      elif inv_action2 == "2":
        print("")

  elif inv_action = "4":
    inv_action2 = input("Do What With This Item?\n1.Use\n2.Throw Away")
    if inv_action2 == "1":
      print("")
      elif inv_action2 == "2":
        print("")

  elif inv_action = "5":
    inv_action2 = input("Do What With This Item?\n1.Use\n2.Throw Away")
    if inv_action2 == "1":
      print("")
      elif inv_action2 == "2":
        print("")


  
# Player stats here ->
HP = 10
ATT = 10
SPE = 10

#Inventory items here ->
inv_item1 = ""
inv_item2 = ""
inv_item3 = ""
inv_item4 = ""
inv_item5 = ""

newgame()
name()
introduction()
