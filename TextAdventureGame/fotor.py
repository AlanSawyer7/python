# Text Adventure Game - Fellowship of the Onion Ring

#globals
player_inventory = ["wallet", "truck keys", "box cutter"]
player_location = "Hobbs Hamburgers"
game_running = True
coworkers = ["your boss", "Timmy", "Sam", "Fred"]
traveling_party = coworkers[1:4]
enemies = ["road_rage_driver", "angry_pedestrian", "lost_hiker"]    
friendlies = ["helpful_motorist", "kind_stranger", "friendly_dog"]
loot = ["onion_rings", "fries", "soda", "ketchup_packets", "crumpled_bill", "coins"] 
bible_quotes = ["Psalm 23:4 - Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.",
                "Proverbs 3:5 - Trust in the Lord with all your heart and lean not on your own understanding;",
                "Isaiah 41:10 - So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand."] 

# location data structure
locations = { 
    "Hobbs Hamburgers": {
        "exits": {"north" : "the truck"},
        "description": "A large roundish brick building with a huge, golden brown, \nplastic onion ring firmly attached to the top on a gray pole",
        "npcs": coworkers
     },

    "the truck": { 
        "exits": { "south" : "Hobbs Hamburgers", "north" : "the highway" },
        "description": "A large red and white box truck with the logo 'Hobbs Hamburgers' on the side. \nThe o is a golden brown onion ring.",
        "npcs": traveling_party
     },

     "the highway": { 
        "exits": { "west" : "gas station" , "east" : "the forest", "north": "a busy stretch" },
        "description": "A busy highway with cars zooming by at high speeds.",
        "npcs": traveling_party + enemies
     },

     "gas station": { 
        "exits": { "east" : "the highway" , "west" : "the diner" },
        "description": "A small gas station with a convenience store. The smell of gasoline fills \nthe air.",
        "npcs": friendlies + traveling_party
     },
    
    "the diner": { 
        "exits": { "east" : "gas station" },
        "description": "A classic American diner with a red and white checkered floor and a \nlong counter with stools.",
        "npcs": friendlies + traveling_party
     },


     "a busy stretch": { 
        "exits": { "south" : "the highway", "north" : "a lonely stretch" },
        "description": "A particularly busy stretch of the highway with honking cars and trucks.",
        "npcs": traveling_party + enemies
     },

# The party gets lost here
     "a lonely stretch": { 
        "exits": { "left" : "the forest" , "right": "a broken down shack" },
        "description": "A quiet, lonely stretch of the highway with little traffic.",
        "npcs": traveling_party + friendlies
     },

# The party gets even more lost here
    "the forest": {
        "exits": { "left" : "a murky pool", "right" : "a dirt path" },
        "description": "A dense forest with tall trees and thick underbrush. The sound of birds chirping fills the air.",
        "npcs": traveling_party + ["a deer", "a squirrel", "a bird"] 
        },

    "a broken down shack": {
        "exits": { "left" : "a lonely stretch", "right": "an abandoned cabin" },
        "description": "An old, broken down shack with peeling paint and a sagging roof.",
        "npcs": traveling_party
        },
    "a murky pool": {
        "exits": { "left" : "a sparkling stream", "right" : "the forest"},
        "description": "A murky pool of water surrounded by tall grass and reeds.",
        "npcs": traveling_party + ["a frog", "a fish"]
        },
    "a dirt path": {
        "exits": { "left" : "the forest", "right": "a muddy stream" },
        "description": "A narrow dirt path winding through the forest.",
        "npcs": traveling_party + ["a rabbit", "a fox"]
        },
    "an abandoned cabin": {
        "exits": { "left" : "a broken down shack", "right": "dark cave" },
        "description": "An old, abandoned cabin with boarded up windows and a creaky door.",
        "npcs": traveling_party + ["a raccoon", "an owl"]
        },
    "a sparkling stream": {
        "exits": { "left" : "a tunnel", "right": "a murky pool" },
        "description": "A clear, sparkling stream flowing through the forest.",
        "npcs": traveling_party + ["a turtle", "a dragonfly"]
        },
    "a muddy stream": {
        "exits": { "left" : "a dirt path", "right": "a waterfall" },
        "description": "A muddy stream with brown, murky water.",
        "npcs": traveling_party + ["a beaver", "a heron"]
        },
    "dark cave": {
        "exits": { "left" : "an abandoned cabin", "right": "a hidden grotto" },
        "description": "A dark, damp cave with stalactites hanging from the ceiling.",
        "npcs": traveling_party + ["a bat", "a spider"]
        },
    "a tunnel": {
        "exits": { "left" : "a mountain pass", "right": "a sparkling stream" },
        "description": "A narrow tunnel carved through the rock.",
        "npcs": traveling_party + ["a mole", "a salamander"]
        },
    "a waterfall": {
        "exits": { "left" : "a muddy stream", "right": "a rainbow pool" },
        "description": "A beautiful waterfall cascading down a rocky cliff.",
        "npcs": traveling_party + ["a kingfisher", "a dragon"]
        },
    "a hidden grotto": {
        "exits": { "left" : "dark cave", "right": "a secret meadow" },
        "description": "A hidden grotto with sparkling crystals and a small pool of water.",
        "npcs": traveling_party + ["a fairy", "a unicorn"]
        },
    "a mountain pass": {
        "exits": { "left" : "a snowy peak", "right": "a tunnel" },
        "description": "A narrow mountain pass with steep cliffs on either side.",
        "npcs": traveling_party + ["a mountain goat", "an eagle"]
        },
    "a rainbow pool": {
        "exits": { "left" : "a waterfall", "right": "a crystal cave" },
        "description": "A pool of water that shimmers with all the colors of the rainbow.",
        "npcs": traveling_party + ["a seal"] 
        },
    "a secret meadow": {
        "exits": { "left" : "a hidden grotto", "right": "a flower field" },
        "description": "A secret meadow filled with colorful wildflowers and tall grass.",
        "npcs": traveling_party + ["a butterfly", "a grasshopper"]
        },
    "a snowy peak": {
        "exits": { "left" : "a cliff face", "right": "a mountain pass"},
        "description": "A snowy peak with a breathtaking view of the surrounding mountains.",
        "npcs": traveling_party + ["a goat"]
        },
    "a crystal cave": {
        "exits": { "left" : "a rainbow pool", "right": "a glittering chamber" },
        "description": "A cave filled with glittering crystals that reflect the light.",
        "npcs": traveling_party + ["a glowing book", "a shining scroll"]
        },
    "a flower field": {
        "exits": { "left" : "a secret meadow", "right": "large building" },
        "description": "A vast field filled with colorful flowers of all kinds.",
        "npcs": traveling_party + ["a bee", "a ladybug"]
        },
    "a cliff face": {
        "exits": { "right" : "a snowy peak"},
        "description": "A steep cliff face with jagged rocks and a sheer drop to the valley below.",
        "npcs": traveling_party + ["a hawk"]
        },
    "a glittering chamber": {
        "exits": { "left" : "a crystal cave" },
        "description": "A chamber filled with glittering treasures and precious gems.",
        "npcs": traveling_party + ["a treasure chest", "a golden crown"]
        },
    "large building": {
        "exits": { "left" : "a flower field" },
        "description": "A large building with tall pillars and a grand entrance.",
        "npcs": traveling_party + ["a guard", "a receptionist"]
    },
}

# print header and welcome message
def print_header():
    print(80*"=")
    print(18*" " + "Welcome to the Fellowship of the Onion Ring!")
    print(80*"=")
    print("\n")

def get_player_name() -> str:
    name = input("What's your name? ")
    return name if name != "" else "Dingus"

def initial_dialog(player_name: str):
    #initial dialog with boss
    print("\\(0 0)/")
    print("  .|.")
    print("   O")
    print("   -")
    print(f"\n{player_name}! Are you daydreaming again? We have to get those onion rings, \nwe're running low. Did you hear a word I said?\n") 
    response = input("Possible responses are: (cry, no, yes) ")
    
    print("-----")
    if response == "cry":
        print(f"You break down in tears. Your boss hands you a handkerchief to wipe your eyes,\n then yells at you 'Get out to the truck!'")
        player_inventory.append("handkerchief")
    elif response == "no":
        print(f"Your boss rolls his eyes and yells 'Get out to the truck!'")
    elif response == "yes":
        print(f"Boss: Great! Now get to the truck")
    else:
        print(f"Your boss sighs. I'm too old for this.")
    print(80*"-")
    
def print_location():
    print(80*"-")
    print(f"You are at {player_location}.")
    print(locations[player_location]["description"])
    print(5*"=")
    if locations[player_location]["npcs"]:
         print(f"(0 0) You see: {', '.join(locations[player_location]['npcs'])}")
         print("  ^")
         print(" \\-/\n")	
    print("------> Exits: " + ", ".join(locations[player_location]["exits"].keys()))

# display player inventory as a list
def show_inventory():
    print(f"You have: {", ".join(player_inventory)}")

def main(): 
    global player_location
    global game_running 

    print_header()

    #ask for player name and start dialog
    player_name = get_player_name()

    initial_dialog(player_name)

    # Game logic loop
    while game_running:
        print_location()

        # Parse the player's input. The input can be 'move [direction]', 'talk [target]', 'inventory', or 'quit'.
        # target is used to retain the case of the npc name when talking
        # target is also used to store the direction for move command
        user_input = input("What do you want to do? (move [direction], talk [target], inventory, quit) ")
        command_list = user_input.split()

        # Make the command lowercase for easier parsing
        command = command_list[0].lower()

        # set target for talk and move commands
        target = command_list[1] if len(command_list) > 1 else ""
        
        #clear screen
        print(100*"\n")

        if command == "move":
            direction = target
            if direction == "":
                direction = input("Where do you want to go? ")
            elif direction in locations[player_location]["exits"]:
                player_location = locations[player_location]["exits"][direction]
                print(f"You move to {player_location}.\n")
            else:
                print("You can't go that way.\n")
        elif command == "talk":
            npc = target  
            if npc == "":   
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
