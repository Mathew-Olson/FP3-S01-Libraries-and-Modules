#-------------------------------
# FP3-S01 Libraries and Modules
# Mathew Thomas Olson
# 15 April 2024
#-------------------------------
# Modules
import time
import random
from Rooms import*
from Actions import*
from MagicNumbers import*

#Main code
game = True
while game == True:
    current_weapon = nothing
                                                                   #introduction
    inventory_battle  = []
    print(""" You wake surounded in darkness. all you can feel is the discomfort of a stone slab across your back. 
    As you start to get up you try to recall who you are and how you got here.""")
    name = input("What was your name again? >")
    print(f"Ah yes, your name was {name}.")
    print("As you start to find your surrounds you find a backpack with some supplies in it ")
    print("You also find a rusty dagger. it does 3-5 damage.")
    current_weapon = weapon_equip(rusty_dagger)
    print("You are currently wielding ", current_weapon[0])
    print("After lighting a torch you see two doors. one of them is red, one of them is a mossy green")
    choice = input("Which door do you want to open? >")
    while not 'red' in choice.lower() and  not 'green' in choice.lower():
        choice = input("that was not one of the options\nWhich door do you want to open? >")

    if 'red' in choice.lower(): 
        red_room(num_of_rooms, current_weapon, inventory_utility, inventory_battle, HP, AC)
    elif 'green' in choice.lower():
        green_room(num_of_rooms, current_weapon, inventory_utility, inventory_battle, HP, AC)
    else:
        print("ERROR")
    
    choice = input("would you like to play again? ")
    if 'n' in choice:
        break