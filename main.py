print('''   

   _                   _      
  (_)                 | |     
   _ _   _ _ __   __ _| | ___ 
  | | | | | '_ \ / _` | |/ _ \
  | | |_| | | | | (_| | |  __/
  | |\__,_|_| |_|\__, |_|\___|
 _/ |             __/ |       
|__/             |___/   



                    /~\/~\/~\
                 /\~/~\/~\/~\/~\
               ((/~\/~\/~\/~\/~\))
             (/~\/~\/~\/~\/~\/~\/~\)
            (////     ~   ~     \\\\)
            (\\\\(   (0) (0)   )////)
            (\\\\(   __\-/__   )////)
             (\\\(     /-\     )///)
              (\\\(  (""""")  )///)
               (\\\(  \^^^/  )///)
                (\\\(       )///)
                  (\/~\/~\/~\/)         **
                    (\/~\/~\/)        *####*
                     |     |           ****
                    /| | | |\            \\
                 _/  | | | | \_ _________//   
                (,,)(,,)_(,,)(,,)--------'






''')

print("Welcome to the Adventure Journey!")
print("Shadi is lost in the Jungle.")
print("Help Shadi find home.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'Which one do you choose to get to other side of '
                    'the lake?'
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the other side of the lake."
                        "There is a Lion waiting for you."
                        "You have three choices:stone, wood, run."
                        "Which colour do you choose?\n").lower()
        if choice3 == "stone":
            print("You can't kill a Lion. Game over.")
        elif choice3 == "wood":
            print("Lion eats you.Game over.")
        elif choice3 == "run":
            print("You are escaping from a lion")
        else:
            print("Lion eats you. Game Over.")

        choice4 = input("You arrive at a house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("Shadi is now home. You win !")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

else:
    print("You got attacked by an angry trout. Game Over.")




















