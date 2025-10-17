# Activity - Choose Your Own Adventure
# 24 September
# Timmie Tang

# Choose Your Own Adventure

# Introduction - Greet the user.
import time

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
greeting = "Welcome to the Choose Your Own Adventure game inspired by Coraline!"

# Print the statement
print(greeting)
print("-DISCLAIMER-THIS GAME MAY BE BROKEN, NO GUARANTEE OF COMEPLETE FUNCTION. ")
# Ask the user if they would like to begin
print("Would you like to begin? (yes/no)")
response = input()

if response == "yes":
    print(" ")
    print("loading...")
    time.sleep(4)
    # Begin the first branch
    print("You are now arriving to the new house mother and father picked out.")
    time.sleep(2)
    print("I heard its haunted...")
    time.sleep(2)
    # Ask the user where they'd like to explore
    explore = input(
        "Would you like to explore the pink palace or the front yard? (pink palace/front yard)"
    )

    if explore == "front yard":
        print(" ")
        print("As you walk through the front yard a boy walks up to you.")
        time.sleep(3)
        print("'Hi, I'm Wybie whats's your name?'")
        time.sleep(2)
        print("You: 'I'm Coraline.'")
        time.sleep(2)
        print("'Caroline what?'")
        time.sleep(2)
        print("You: 'Coraline! Coraline Jones.'")
        time.sleep(2)
        print(
            "Wybie tells you about how he's never been in the pink palace because his grandma doesn't let him."
        )
        time.sleep(3)
        print(
            "'My grandma, she owns the pink palace. Says her twin sister went missing in there and it's too dangerous.'"
        )
        time.sleep(5)
        print("Wybie leaves you to explore on your own.")
        time.sleep(5)

        # Ask the user
        print(
            "You make your way back the pink palace where the both mother and father are busying working on their computers."
        )
        time.sleep(5)
        print("You wonder off to explore the house and stumble across a mini door.")
        time.sleep(3)
        open_door = input("Do you enter the door? (yes/no)")
        if open_door == "yes":
            print(" ")
            print(
                "The door leads to a ditch and you fall to your death. Play again for a different outcome."
            )
        elif open_door == "no":
            print(" ")
            print(
                "You skip the door and walk to a different room where a black cat watches you out the window."
            )
            time.sleep(3)
            print(
                "The black cat leads you to the neighbours house and you get kidnapped."
            )
    elif explore == "pink palace":
        print(" ")
        print("You step into the house as the floor boards creak.")
        print(
            "The house is awful quiet. You walk up to the kitchen to see mother working on her laptop."
        )
        time.sleep(3)
        print("Mother tells you to be quiet and go unpack the boxes.")
        time.sleep(2)
        print(
            "You walk up to the boxes, and spot a white box that sat in the corner of the living room, away from the brown boxes the family had packed."
        )
        time.sleep(5)
        print("The label reads 'DO NOT OPEN', in bright red lettering.")
        time.sleep(3)

    # Ask the user which box they'd like to open
    boxes = input(
        "Do you choose to open the odd box or unpack the boxes like mother instructed you to? (open the odd box/unpack the boxes)"
    )
    time.sleep(4)

    if boxes == "open the odd box":
        print(" ")
        print(
            "You glide the box cutter along the tape to reveal a heavy black key with a button, where the handle should be."
        )
        time.sleep(4)
        # Ask the user where they'd like to keep the key
        print(
            "Would you like to keep this eerie key in your pocket or in your nightstand to keep safe? (keep in my pocket/in my nightstand)"
        )
        time.sleep(3)
        response = input()

        if response == "keep in my pocket":
            print(" ")
            print(
                "The heavy key slips easily into your pocket. You can feel it graze your leg each step you take."
            )
            time.sleep(3)
            print(
                "You head downstairs to the kitchen where mother hands you a newpaper-wrapped package."
            )
            time.sleep(4)
            print("'Some kid dropped this off for you.'")
            time.sleep(2)
            # Ask if the user wants to recieve Wybie's present
            recieve_present = input("Open the present? (yes/yes)")
            if recieve_present == "yes":
                print("You unwrap the wrinkled newspaper..")
                time.sleep(3)
                print(
                    "The note reads 'Hey Jonesy, look what I found in grandma's trunk. Look familiar? -Wybie'"
                )
                time.sleep(4)
                print(
                    "Wybie has gifted you a doll that looks exactly like you, but with buttons sewn in as eyes."
                )

        elif response == "in my nightstand":
            print(" ")
            print(
                "You hop up the stairs gracefully to your room, unfazed by the creeps of this house,"
            )
            time.sleep(2)
            print(
                "You walk past father's room as he types away on his vintage computer in his room full of boxes."
            )
            time.sleep(2)
            print(
                "You drop off the key in your nightstand and scramble back to tell father about all the things you've discovered."
            )
            time.sleep(2)
            print("Father is so busy he ignores you.")
            time.sleep(2)
            print(
                "You head downstairs to the living room where you find a medium sized door."
            )
            time.sleep(2)
            # Ask the user if they want to proceed through the medium door
            fall_door = input("Go through the door? (yes/no)")
            if fall_door == "yes":
                print(" ")
                print("You've fallen into a ditch. Play again for a different outcome.")
            elif fall_door == "no":
                print(" ")
                print("You see a small door next to the medium door.")
                # Ask if the user wants to go in the door
                in_door = input("Step into the small door with your key? (yes/no)")
                if in_door == "yes":
                    print(" ")
                    print("You've discovered the entrance to the 'other world'.")
                    time.sleep(2)
                    proceed_small_door = input("Would you like to proceed? (yes/no")
                    if proceed_small_door == "yes":
                        print(" ")
                        print(
                            "Your 'other mother' sews buttons into your eyes. Play again for a different outcome."
                        )
                elif in_door == "no":
                    print(" ")
                    print("Ok you're lame. Play again for a different outcome.")
    elif boxes == "unpack the boxes":
        print(" ")
        print("You unpacked the boxes to find mother's collection of snow globes.")
        print("You neatly set the snow globes on the window cill.")

elif response == "no":
    print(" ")
    print("aight run the code again and start the game.")
