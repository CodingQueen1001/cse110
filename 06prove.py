choice1 = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. \nWhich one do you want to pick up? ")
print()
if choice1.lower() == "match":
        match1 = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ")
        print()
        if match1.lower() == "run":
            match2 = input("You turn on your heel and take off running in the opposite direction of the bear, but you can hear the bear following behind you. Do you want to KEEP running, FIND someplace to hide or CALL for help? ")
            print()
            if match2.lower() == "keep":
                print("You decided to keep running. Eventually the bear catches up with you, and you die by getting eaten by a bear.")
            elif match2.lower() == "hide":
                print("You decided to try and hide from the bear. The bear eventually finds you, and you die by getting eaten by a bear.")
            elif match2.lower() == "call":
                print("You decided to scream for help and a hunter hears you. He shoots the bear before giving you a ride home and you arrive home safely.")
            else:
                print("That is not an option.")
        elif match1.lower() == "hide":
            match2 = input("You slowly back away and hide behind a tree, but realize you have no idea where you are. Do you want to STAY hidden or go BACK and try to find the trail? ")
            print()
            if match2.lower() == "stay":
                print("You stay hidden but the bear still finds you. You die by getting eaten by a bear.")
            elif match2.lower() == "back":
                print("You find your way back to the trail and a friendly hunter offers to give you a ride back to your car. You arrive home safely.")
            else:
                print("That is not an option.")
elif choice1.lower() == "flashlight":
            light1 = input("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")
            print()
            if light1.lower() == "follow":
                light2 = input("You choose to stay on the path and follow it to a deserted cabin. Do you KNOCK on the door or BREAK a window to sneak in? ")
                print()
                if light2.lower() == "knock":
                    print("You choose to knock on the door and a man answers. He invites you inside and you explain your story to him. He drives you back to your car and you arrive home safely.")
                elif light2.lower() == "break":
                    print("You choose to break a window and sneak into the house. The owner of the house hears you break in and grabs his shotgun. You die from being shot.")
                else:
                    print("That is not an option.")
            elif light1.lower() == "look":
                light2 = input("You turn towards the sound you heard in the woods and start following it. After walking for a while, you notice that the faint howling is getting louder and turn around to see you are face to face with a wolf. Do you want to SCREAM or stand STILL and see if it will leave? ")
                print()
                if light2.lower() == "scream":
                    print("You scream in fear when you see the wolf which attracts the other wolves. You die from being eaten alive by wolves.")
                elif light2.lower() == "still":
                    print("You stand completely still and the wolf stares at you for only a minute before trotting off. You head back the way you came and arrive home safely.")
                else:
                    print("That is not an option.")
            else:
                print("That is not an option.")