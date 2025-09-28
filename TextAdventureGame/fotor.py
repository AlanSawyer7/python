# Text Adventure Game - Fellowship of the Onion Ring

#globals
player_inventory = ["wallet", "truck keys", "box cutter"]
player_location = "Hobbs Hamburgers"

locations = { 
    "Hobbs Hamburgers": {
        "exits": [ "north" ],
        "description": "A large roundish brick building with a huge, golden brown, plastic onion ring firmly attached to the top on a gray pole",
        "npcs": [ "boss", "Timmy", "Sam", "Fred" ]
     },

    "truck": { 
        "exits": [ "north" ],
        "description": "A large red and white box truck with the logo 'Hobbs Hamburgers' on the side. The o is a golden brown onion ring.",
        "npcs": [ "Timmy", "Sam", "Fred" ]
     }
}
	

def show_inventory():
    print(f"You have: {player_inventory}")

def main(): 
    #print header and welcome
    print(44*"=")
    print("Welcome to the Fellowship of the Onion Ring!")
    print(44 *"=")
    print("\n\n")

    #ask for player name and start dialog
    player_name = input("What's your name? ")
    if player_name != "":
        print(f"\n{player_name}! Are you daydreaming again? We have to get those onion rings, we're running low. Did you hear a word I said?\n") 

    response = input("Possible responses are: (cry, no, yes) ")
    print("\n")
    if response == "cry":
        print(f"You break down in tears. Your boss hands you a handkerchief to wipe your eyes, then yells at you 'Get out to the truck!'")
        player_inventory.append("handkerchief")
    elif response == "no":
        print(f"Your boss rolls his eyes and yells 'Get out to the truck!'")
    elif response == "yes":
        print(f"Boss: Great! Now get to the truck")
    else:
        print(f"Your boss sighs. I'm too old for this.")
    print("\n")

    # Game logic would go here
    user_input = input("Press Enter to exit the game.")
    if user_input == "":
        show_inventory()
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
