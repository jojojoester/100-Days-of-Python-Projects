print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right":').lower()
if choice1 == "left":
    #continue in game
    choice2 = input('You have come to a lake, there is an island in the middle of the lake. Type "wait" to wait for the boat or Type "swim" to swim across:').lower()
    
    if choice2 == "wait":
        #continue the game
        choice3 = input('You have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose:').lower()
        
        if choice3 == "red":
            print("You just entered the room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You just entered the room full of beasts. Game Over.")
        elif choice3 == "yellow":
            print("Congratulation!!!!! You just entered the room full of treasures.")
        else:
            print("You choose the door that doesn't exists. Game Over.")
       
    else:
        print("You got attacked by the shark. Game Over.")
               
else:
    print("You fell into the hole. Game Over.")