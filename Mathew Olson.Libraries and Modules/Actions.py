#Actions
import time
import random
from Rooms import*
from MagicNumbers import*

#variables
tree_thing = ['tree creature', 8, 2, 4, 14] #creatures
flesh_golem = ['flesh golem', 15, 5, 8, 12] 
litch = ['litch', 25, 10, 12, 15]


def add_inventory(item):                                                           #adding items to your inventory
    print(f"{item} has been added to your inventory.")  
    inventory_battle.append(item)

def weapon_equip(weapon):                                                          #equiping weapons seperate from inventory
    choice = input(f"would you like to equip the {weapon[0]}? >")
    if 'y' in choice.lower():
        return weapon
    else:
        print("You discard this weapon.")
        return current_weapon 

def combat(enemy, current_weapon, HP, AC):                                         #for fighting creatures
    enemy_hp = enemy[1]                                                            #so the effects don't save between combats
    #print(enemy_hp)
    enemy_low_attk = enemy[2]
    
    enemy_high_attk = enemy[3]
    
    fighting = True                                                                #repeatable turns
    print(f"You have entered combat with {enemy[0]}.")
    while fighting == True:
        
        ###Player turn###
        if HP > 0:                                                                 #if you don't die
            
            print("""\n\nIts your turn, you may:\n
        attack your opponent
        use an item
        wait
        """)
            attack = input("what would you like to do? ")
            while not 'att' in attack.lower() and not 'use' in attack.lower() and not 'wait' in attack.lower(): #make sure they use a valid statement
                print("That was not an option, try again.")
                attack = input("what would you like to do? ")
            
            if 'att' in attack.lower():                                            #normal attack
                print(f"rolling to attack aginst AC{enemy[4]}")
                attack_roll = random.randint(1, 20)
                print(f"You rolled a {attack_roll}")
                
                if attack_roll >= int(enemy[4]):
                    print("you hit")
                    damage = random.randint(current_weapon[1], current_weapon[2])
                    print(f"You deal {damage} damage to {enemy[0]}")
                    enemy_hp -= damage
                    print('They now have ', enemy_hp)
            
                elif attack_roll < enemy[4]:
                    print("You missed")
                
                else:
                    print("error in attack roll")
            

            elif 'use' in attack.lower() or 'item' in attack.lower():             #using items
                
                for position in range(len(inventory_battle)):
                    print(inventory_battle[position], '=', position + 1)
                
                         
                if len(inventory_battle) == 0:                                    #in case the list is empty
                    print("You open your bag only to see that it is empty")
                
                else:
                    item_used = int(input("Which would you like to use? "))
                    item_used = inventory_battle.pop(item_used - 1)
                    if item_used[0] == 'health potion':
                        print('HP was ', HP)
                        HP += item_used[1]
                        print('HP is ', HP)
                
                
                
            
            elif 'wait' in attack.lower():                                        #wait if you want too... for some reason
                print("You like the gentleman you are wait for your opponent to play.")
        
        elif HP <= 0:                                                             #if you die
            fighting = False
            win = False
        
        time.sleep(4)                                                             #to let the player read
        ###Enemy turn###
        if enemy_hp > 0 and HP > 0:                                               #if they don't die
            print(f"\n\nIt is {enemy[0]}'s turn")
            print("They will attack you")                                         #they can only attack right now
            
            print(f"rolling to attack aginst AC{enemy[4]}")
            attack_roll = random.randint(1, 20)
            print(f"You rolled a {attack_roll}")
            
            if attack_roll >= enemy[4]:
                print("Hit")
                damage = random.randint(enemy_low_attk, enemy_high_attk)
                print(f"{enemy[0]} deals {damage} damage to you")
                HP -= damage
                print("You now have ", HP)
        
            elif attack_roll < enemy[4]:
                print("They missed")
            
            else:
                print("error in enemy attack roll")
            
        elif enemy_hp <= 0:                                                       #if they die
            fighting = False
            win = True
        
        time.sleep(4)                                                             #to let the player read


    return win