print(r'''
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

firstQ = input("You found a temple and must go through its passages to uncover the hidden treasure! \n"
                "You must first chose if you want yo go left of right. Type 'L' or 'R \nll").lower()

if firstQ == "R":
    secondQ= input('"You must now choose to swim between 2 different rivers! Pick "L" or "R".\n'
            'Hurry, the path behind you is collapsing"\n').lower()
    if secondQ == "R":
        thirdQ= input('You\'ve come to a to a dark enterance. There is a lever you can pull to'
                      'possibly get some light or you can continue in the dark.'
                      'Type "continue" to go in the dark or "pull"...\n').lower()
        if thirdQ == "pull":
        else:
            print("🦂You ran into a pit half way through and fell into a bed of scorpions🦂")
    else:
        print("🦈You got ate by sharks🦈")
else:
    print("🐍You have fallen into a pit of snakes🐍")

