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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to treasure Island\n Your mission is to find the treasure")
print("Let's Begin")
choice1= input("You are on a cross road,you need to decide in which direction you wanna go. \n"
              " 1-> Left "
              " 2-> Right "
              " 3-> Straight\n")
if choice1 == "1":
    print("You have arrived infront of an ocean")
    choice2= input("Do you wanna wait on the beach,so that a ship can find you?\n "
                   "then type Wait\n"
                   " or \n"
                   "explore the beach to find materials to build a boat of your own?\n"
                   "then type Explore\n").lower()
    if choice2 == "wait":
        print("You have waited for too long but no ship arrived,"
              "and now you are stranded in this island forever\n"
              "AHAHAHAHA! You lazy sack of potato! GAME OVER ")
    elif choice2 == "explore":
        print("Congratulations you have find a light house!!!")
        choice3= input(" Want to go ask for help? Y/N\n").lower()
        if choice3 == "y":
            search=input("The light house seems empty,"
                         "do you wanna continue your search alone?y/n\n").lower()
            if  search =="y":
                print("*Dont forget to take the torch and the saw with you before leaving.*")
                tree=input("You have found a tree do you wanna chop it?y/n\n").lower()
                if tree=="y":
                    print("Congratulation now you can start building your boat")
                    print("Your boat is ready.\n"
                          "Now you can start sailing and reach the treasure Island")
                    island=input("Can you see the land infront of you? Y/N\n").lower()
                    if island== "y":
                        print("Congratulations!!! You have safely reached the Island")
                        door= input("There are three door infront of you."
                                    "RED,BLUE and BLACK\n"
                                    "Which one do you wanna enter?").lower()
                        if door== "red":
                            print("OPPS!! "
                                  "There was fire behind this door and you are burnt to death."
                                  " GAME OVER!!")
                        elif door=="blue":
                            print("Congratulation you have found the treasure.!! You won!!")
                        elif door=="black":
                            print("OPPS!! there was a Black Hole behind this door and you are sucked into it."
                                  "GAME OVER!!")
                        else:
                            print("you have entered a wrong input")

                    else:
                        print("OPPS!! looks like you are lost in the sea."
                              "GAME OVER")
                elif tree=="n":
                    print("You are a good person.!! "
                          "But that won't make you survive here."
                          "GAME OVER")
                else:
                    print("you have entered a wrong input")
            elif search == "n":
                print("You are a scaredy cat!!! GAME OVER")
            else:
                print("you have entered a wrong input")
        elif choice3=="n":
            print("You are too arrogant to ask for help. DIE ALONE!!! GAME OVER")
        else:
            print("you have entered a wrong input")

elif choice1 =="2":
    print("You have reached a desert")
    print("Due to lack of water and extreme heat you will die."
          " GAME OVER!!!")

elif choice1 =="3":
    print("Now you are lost in a jungle")
    decision=input("Do you wanna keep walking? Y/N\n").lower()
    if decision=="y":
        print("OPPS!! you have walked into a lion's den and they made you their brunch!!")
    elif decision=="n":
        print("Because you were in the same place for so long a grizzly bear found you\n"
              " and now you are going to be part of it's hibernation storage")
    else:
        print("you have entered a wrong input")

else:
    print("Game over")