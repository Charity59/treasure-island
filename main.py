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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

position = input("Would you like to go to the right or left?\n")
position_case = position.lower()

if position_case == "left":
  swim_or_wait = input("Do you want to swim or wait?\n")
  swim_or_wait_case = swim_or_wait.lower()
  if swim_or_wait_case == "wait":
    door = input("Which door would you like to go? Red, Blue or Yellow\n")
    door_case = door.lower()
    if door_case == "red":
      print("Oh! Burned by fire. Game Over.")
    elif door_case == "blue":
      print("You enter a room of beasts. Game Over.")
    elif door_case == "yellow":
      print("You found the treasure! You Win.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("Attack by trout. Game Over")
else:
  print("Game Over! You have fallen into a hole ")
  
