# Text Adventure Game - Fellowship of the Onion Ring

#globals
player_inventory = ["wallet", "truck keys", "box cutter"]
player_location = "Hobbs Hamburgers"
game_running = True
coworkers = ["your boss", "Timmy", "Sam", "Fred"]
traveling_party = coworkers[1:4]
enemies = ["road rage driver", "angry pedestrian", "lost hiker"]    
friendlies = ["helpful motorist", "kind stranger", "friendly dog"]
loot = ["onion rings", "fries", "soda", "ketchup packets", "crumpled bill", "coins"] 
bible_quotes = ["Psalm 23:4 - Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.",
                "Proverbs 3:5 - Trust in the Lord with all your heart and lean not on your own understanding;",
                "Isaiah 41:10 - So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand."] 

# location data structure
locations = { 
    "Hobbs Hamburgers": {
        "exits": {"north" : "the truck"},
        "description": "A large roundish brick building with a huge, golden brown, plastic onion ring firmly attached to the top on a gray pole",
        "npcs": coworkers
     },

    "the truck": { 
        "exits": { "south" : "Hobbs Hamburgers", "north" : "the highway" },
        "description": "A large red and white box truck with the logo 'Hobbs Hamburgers' on the side. The o is a golden brown onion ring.",
        "npcs": traveling_party
     },

     "the highway": { 
        "exits": { "west" : "gas station" , "east" : "the forest", "north": "a busy stretch" },
        "description": "A busy highway with cars zooming by at high speeds.",
        "npcs": enemies
     },

     "gas station": { 
        "exits": { "east" : "the highway" , "west" : "the diner" },
        "description": "A small gas station with a convenience store. The smell of gasoline fills the air.",
        "npcs": friendlies + traveling_party
     },
    
    "the diner": { 
        "exits": { "east" : "gas station" },
        "description": "A classic American diner with a red and white checkered floor and a long counter with stools.",
        "npcs": friendlies + traveling_party
     },


     "a busy stretch": { 
        "exits": { "south" : "the highway", "north" : "a lonely stretch" },
        "description": "A particularly busy stretch of the highway with honking cars and trucks.",
        "npcs": enemies
     },

# The party gets lost here
     "a lonely stretch": { 
        "exits": { "left" : "the forest" , "right": "a broken down shack" },
        "description": "A quiet, lonely stretch of the highway with little traffic.",
        "npcs": friendlies
     },

# The party gets even more lost here
    "the forest": {
        "exits": { "left" : "a murky pool", "right" : "a dirt path" },
        "description": "A dense forest with tall trees and thick underbrush. The sound of birds chirping fills the air.",
        "npcs": ["a deer", "a squirrel", "a bird"] 
        },


}
	
# display player inventory as a list
def show_inventory():
    print(f"You have: {", ".join(player_inventory)}")

def main(): 
    global player_location
    global game_running 

    #print header and welcome
    print(44*"=")
    print("Welcome to the Fellowship of the Onion Ring!")
    print(44 *"=")
    print("\n")

    #ask for player name and start dialog
    player_name = input("What's your name? ")
    if player_name != "":
        print(f"\n{player_name}! Are you daydreaming again? We have to get those onion rings, we're running low. Did you hear a word I said?\n") 
    else:
        player_name = "Dingus"
        print(f"\nDingus! Are you daydreaming again? We have to get those onion rings, we're running low. Did you hear a word I said?\n")
    response = input("Possible responses are: (cry, no, yes) ")
    print(100*"\n")
    
    if response == "cry":
        print(f"You break down in tears. Your boss hands you a handkerchief to wipe your eyes, then yells at you 'Get out to the truck!'")
        player_inventory.append("handkerchief")
    elif response == "no":
        print(f"Your boss rolls his eyes and yells 'Get out to the truck!'")
    elif response == "yes":
        print(f"Boss: Great! Now get to the truck")
    else:
        print(f"Your boss sighs. I'm too old for this.")
    print(30*"*" + "\n")

    # Game logic would go here
    while game_running:
        print(f"You are at {player_location}.")
        print(locations[player_location]["description"])
        print(f"Exits: {", ".join(list(locations[player_location]['exits'].keys()))}")
        print(f"You see: {", ".join(locations[player_location]['npcs'])}")
        print("\n")

        command = input("What do you want to do? (move, talk, inventory, quit) ")
        print(100*"\n")

        if command == "move":
            direction = input("Where do you want to go? ")
            if direction in locations[player_location]["exits"]:
                player_location = locations[player_location]["exits"][direction]
                print(f"You move to {player_location}.\n")
            else:
                print("You can't go that way.\n")
        elif command == "talk":
            talk_to = ", ".join(locations[player_location]["npcs"])
            npc = input("Who do you want to talk to? (" + talk_to + ") ")
            if npc in locations[player_location]["npcs"]:
                print(f"You talk to {npc}. They greet you warmly.\n")
            else:
                print(f"There is no {npc} here.\n")
        elif command == "inventory":
            show_inventory()
            print("\n")
        elif command == "quit":
            print("Exiting the game...\n")
            break
        else:
            print("Invalid command. Please try again.\n")

    print("Thanks for playing the Fellowship of the Onion Ring!")

if __name__ == "__main__":
    main()
