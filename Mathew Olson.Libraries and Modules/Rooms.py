#Rooms
import time
import random
from Actions import*
from MagicNumbers import*


def red_room(num_of_rooms, current_weapon, inventory_ultility, inventory_battle, HP, AC):                                                       #flesh golem encounter
    num_of_rooms += 1
    print(""" 
 As you enter you are shocked at the sight of blood
 covering nearly every surface in this room
 but it does not take you long to find out why.
 within moments of entering the room you see a
 large flesh golem standing at the other end of the room with
 fists bloodied from what you can only assume were previous adventurers.""")
    
    time.sleep(4)
    
    choice = input("""
 Seeing this gruesome sight you:
attack this monster to get revenge for the fallen.
Run away in terror.
try to talk to it.
what do you do? """)
    if 'fig' in choice.lower() or 'att' in choice.lower():
        win = combat(flesh_golem, current_weapon, HP, AC)
        if win == True:
            print("You defeated the flesh_golem")
            print("You see a pedistal in the center of the room that has a great axe on it.")
            current_weapon = weapon_equip(great_axe)
            print(" You also find a health potion")
            add_inventory(health_potion)
            
            time.sleep(1)
            if num_of_rooms < 2:
                choice = input("""you see a dark door at the end of the room. looking at it gives you a sense of no return.
    would you like to go through the dark door or investigate green door? """)
                if 'green' in choice.lower():
                    green_room(num_of_rooms, current_weapon, inventory_ultility, inventory_battle, HP, AC)
                    
                elif 'dark' in choice.lower() or 'end' in choice.lower():
                    final_battle(current_weapon, inventory_utility, inventory_battle, HP, AC)
            
            else:
                print("""knowing there is nothing else to do but continue you
    go through the door to face the litch""")
                time.sleep(2)
                final_battle(current_weapon, inventory_utility, inventory_battle, HP, AC)
            
        elif win == False:
            print("You have died")
            

    elif 'talk' in choice.lower():
        print("you attempt to talk to this creature but It doesn't seem to listen as it starts to run towards you")

        win = combat(flesh_golem, current_weapon, HP, AC)
        if win == True:
            print("\nYou defeated the flesh_golem")
            print("You see a pedistal in the center of the room that has a great axe on it.")
            current_weapon = weapon_equip(great_axe)
            print(" You also find a health potion")
            add_inventory(health_potion)
            
            time.sleep(1)
            if num_of_rooms < 2:
                choice = input("""you see a dark door at the end of the room. looking at it gives you a sense of no return.
    would you like to go through the dark door or investigate green door? """)
                if 'green' in choice.lower():
                    green_room(num_of_rooms, current_weapon, inventory_ultility, inventory_battle, HP, AC)
                    
                elif 'dark' in choice.lower() or 'end' in choice.lower():
                    final_battle(current_weapon, inventory_utility, inventory_battle, HP, AC)
            
            else:
                print("""knowing there is nothing else to do but continue you
    go through the door to face the litch""")
                time.sleep(2)
                final_battle(current_weapon, inventory_utility, inventory_battle, HP, AC)
            
            
        elif win == False:
            print("You have died")
            
        

    elif 'run' in choice.lower():
        print("You turn around and sprint as fast as you can chosing the green room instead.")
        green_room(num_of_rooms, current_weapon, inventory_utility, inventory_battle, HP, AC)
            
            
    

def green_room(num_of_rooms, current_weapon, inventory_utility, inventory_battle, HP, AC):                                                    #tree thing encounter
    num_of_rooms += 1
    print("""
You enter a room full of faint lights. Plants litter the entire room and you can see they
  are the main source of these lights with some plants having a strange glow to them.
  as you walk through this room some of the plants moving towards you as they shift
  and transform into a humanoid creature.""")
    time.sleep(2)
    print("""Seeing this you:
Attack it.
Try and talk to it.
Run away.""")
    choice = input("What do you do? ")

    if 'attack' in choice.lower() or 'fight' in choice.lower():                                                                                #fighting the creature
        win = combat(tree_thing, current_weapon, HP, AC)
        if win == True:
            print("\nYou defeated the tree creature")
            print("You find a piece of wood that you could use as a shield. +2 AC")
            AC += 2
            time.sleep(1)
            if num_of_rooms < 2:
                choice = input("""
    you see a dark door at the end of the room and have the impression that if you go through you may not return
    do yo or investigate the red room from earlier.""")
                if 'red' in choice.lower():
                    red_room(num_of_rooms, current_weapon, inventory_utility, inventory_battle, HP, AC)
                elif 'dark' in choice.lower() or 'end' in choice.lower():
                    print("You go through the door to face the litch")
                    time.sleep(1)
                final_battle(current_weapon, inventory_utility, inventory_battle, HP, AC)
            else:
                print("""knowing there is nothing else to do but fight you
    go through the door to face the litch""")
                time.sleep(2)
                final_battle(current_weapon, inventory_utility, inventory_battle, HP, AC)
            
                
            
        if win == False:
            print("You have died")
            
        
    
    elif 'talk' in choice.lower():
        print("Turns out its friendly and it tells you about the place you are")
        print('''"This place used to be a wonderful place full of plants and creatures of dozens of varieties"
"But one day the lich found it and has been corupting it since killing all that it finds and adding them to
his undead army. If you continue any further you will have to face the litch"
seeing that you plan to continue anyway they offer
you a weapon that may help in your fight with the litch.''')
        
        time.sleep(2)
        
        current_weapon = weapon_equip(grass_cutter)
        if num_of_rooms < 2:
            choice = input("do you want to fight the litch or investigate the red room from earlier.")
            if 'red' in choice.lower():
                red_room(num_of_rooms, current_weapon, inventory_utility, inventory_battle, HP, AC)
            elif 'litch' in choice.lower():
                print("You go through the door to face the litch")
                time.sleep(1)
                final_battle(current_weapon, inventory_utility, inventory_battle, HP, AC)
        else:
            print("""knowing there is nothing else to do but fight you
go through the door to face the litch""")
            time.sleep(4)
            final_battle(current_weapon, inventory_utility, inventory_battle, HP, AC)
            
        
    elif 'run' in choice.lower():
        print("You sprint past the creature and run through the nearest door without looking back.")
        red_room(num_of_rooms, current_weapon, inventory_utility, inventory_battle, HP, AC)
        
        
    else:
        print("seeing as your too shocked to talk properly you will run away")
        print("You sprint past the creature and run through the nearest door without looking back.")
        red_room(num_of_rooms, current_weapon, inventory_utility, inventory_battle, HP, AC)

    
    
def final_battle(current_weapon, inventory_utility, inventory_battle, HP, AC): #battle to fight the litch
    print("""As you enter this room you are engulfed in  a darkness that your torch can only fight back to an extent.
You can't see any of the walls to this room except for the one you entered from and even that disappears as you investigate further.
You can hear a faint chanting in the distance that you decide to investigate further.""")
    time.sleep(4)
    win = combat(litch, current_weapon, HP, AC)
    if win == True: #if you kill the litch
        print(""" As the litch falls the darkness that seems to envelope the room disipates.
It seems that whatever had befallen this place died when the litch fell.
after a couple of hours of searching you eventually find you way to the surface,
and start your adventure to find out who you are.""")
        
    
    else: #if the litch kils you
        print(""" As you feel you life force fading from your body you can
start to feel an evil magic coursing through your veins and know that
this was not your end""")