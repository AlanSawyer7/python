# Text Adventure Game - Fellowship of the Onion Ring

#globals
player_inventory = ["wallet", "truck_keys", "box_cutter"]
player_location = "Hobbs Hamburgers"
game_running = True
coworkers = ["Boss", "Timmy", "Sam", "Fred"]
traveling_party = coworkers[1:4]
enemies = ["road_rage_driver", "angry_pedestrian", "lost_hiker"]    
friendlies = ["helpful_motorist", "kind_stranger", "friendly_dog"]
bible_quotes = ["Psalm 23:4 - Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.",
                "Proverbs 3:5 - Trust in the Lord with all your heart and lean not on your own understanding;",
                "Isaiah 41:10 - So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand."] 

# Possible vehicles to use
vehicles = {
    "truck": {
        "started": False,
        "fuel": 100,
        "rate": 10, #fuel consumption rate
        "capacity": 50, #bags of onion rings
        "uses": "drive",
    },
    "car": {
        "started": False,
        "fuel": 50,
        "rate": 7, #fuel consumption rate
        "capacity": 5, #bags of onion rings
        "uses": "drive",
    },
    "motorbike": {
        "started": False,
        "fuel": 25,
        "rate": 2, #fuel consumption rate
        "capacity":2, #bags of onion rings
        "uses": "ride",
    },
    "bike": {
        "started": True,
        "fuel": 0,
        "rate": 0, #fuel consumption rate
        "capacity":1, #bags of onion rings
        "uses": "ride",
    }

}
# currently used vehicle, movement decreases fuel amount increases capacity
current_vehicle = None

# location data structure
locations = { 
    "Hobbs Hamburgers": {
        "exits": {"north" : "the truck"},
        "description": "A large roundish brick building with a huge, golden brown, \nplastic onion ring firmly attached to the top on a gray pole",
        "npcs": coworkers,
        "items": ["onion_rings", "fries", "soda" ],
        "vehicles": []
     },
    "the truck": { 
        "exits": { "south" : "Hobbs Hamburgers", "north" : "the highway" },
        "description": "A large red and white box truck with the logo 'Hobbs Hamburgers' on the side. \nThe o is a golden brown onion ring.",
        "npcs": traveling_party,
        "items": ["ketchup_packets", "crumpled_bill", "coins", "gloves" ],
        "vehicles": ["truck"]
     },
     "the highway": { 
        "exits": { "west" : "gas station" , "east" : "the forest", "north": "a busy stretch" },
        "description": "A busy highway with cars zooming by at high speeds.",
        "npcs": traveling_party + enemies,
        "items": [],
        "vehicles": []
     },
     "gas station": { 
        "exits": { "east" : "the highway" , "west" : "the diner" },
        "description": "A small gas station with a convenience store. The smell of gasoline fills \nthe air.",
        "npcs": friendlies + traveling_party,
        "items": ["bible", "map", "car_keys" ],
        "vehicles": ["car"]
     },
    "the diner": { 
        "exits": { "east" : "gas station" },
        "description": "A classic American diner with a red and white checkered floor and a \nlong counter with stools.",
        "npcs": friendlies + traveling_party,
        "items": ["coffee", "pie", "ashtray", "lighter" ],
        "vehicles": []
     },
     "a busy stretch": { 
        "exits": { "south" : "the highway", "north" : "a lonely stretch" },
        "description": "A particularly busy stretch of the highway with honking cars and trucks.",
        "npcs": traveling_party + enemies,
        "items": [],
        "vehicles": []
     },
# The party gets lost here
     "a lonely stretch": { 
        "exits": { "left" : "the forest" , "right": "a broken down shack" },
        "description": "A quiet, lonely stretch of the highway with little traffic.",
        "npcs": traveling_party + friendlies,
        "items": [],
        "vehicles": []
     },

# The party gets even more lost here
    "the forest": {
        "exits": { "left" : "a murky pool", "right" : "a dirt path" },
        "description": "A dense forest with tall trees and thick underbrush. The sound of birds chirping fills the air.",
        "npcs": traveling_party + ["a deer", "a squirrel", "a bird"],
        "items": [],
        "vehicles": []
        },
    "a broken down shack": {
        "exits": { "left" : "a lonely stretch", "right": "an abandoned cabin" },
        "description": "An old, broken down shack with peeling paint and a sagging roof.",
        "npcs": traveling_party,
        "items": ["shovel", "rope" ],
        "vehicles": []
        },
    "a murky pool": {
        "exits": { "left" : "a sparkling stream", "right" : "the forest"},
        "description": "A murky pool of water surrounded by tall grass and reeds.",
        "npcs": traveling_party + ["a frog", "a fish"],
        "items": ["fishing rod", "bait" ],
        "vehicles": []
        },
    "a dirt path": {
        "exits": { "left" : "the forest", "right": "a muddy stream" },
        "description": "A narrow dirt path winding through the forest.",
        "npcs": traveling_party + ["a rabbit", "a fox"],
        "items": [],
        "vehicles": ["bike"]
        },
    "an abandoned cabin": {
        "exits": { "left" : "a broken down shack", "right": "dark cave" },
        "description": "An old, abandoned cabin with boarded up windows and a creaky door.",
        "npcs": traveling_party + ["a raccoon", "an owl"],
        "items": ["flashlight", "batteries", "bandages" ],
        "vehicles": []
        },
    "a sparkling stream": {
        "exits": { "left" : "a tunnel", "right": "a murky pool" },
        "description": "A clear, sparkling stream flowing through the forest.",
        "npcs": traveling_party + ["a turtle", "a dragonfly"],
        "items": ["cup", "water bottle" ],
        "vehicles": []
        },
    "a muddy stream": {
        "exits": { "left" : "a dirt path", "right": "a waterfall" },
        "description": "A muddy stream with brown, murky water.",
        "npcs": traveling_party + ["a beaver", "a heron"],
        "items": ["boot"],
        "vehicles": []
        },
    "dark cave": {
        "exits": { "left" : "an abandoned cabin", "right": "a hidden grotto" },
        "description": "A dark, damp cave with stalactites hanging from the ceiling.",
        "npcs": traveling_party + ["a bat", "a spider"],
        "items": ["pickaxe", "helmet" ],
        "vehicles": []
        },
    "a tunnel": {
        "exits": { "left" : "a mountain pass", "right": "a sparkling stream" },
        "description": "A narrow tunnel carved through the rock.",
        "npcs": traveling_party + ["a mole", "a salamander"],
        "items": [],
        "vehicles": []
        },
    "a waterfall": {
        "exits": { "left" : "a muddy stream", "right": "a rainbow pool" },
        "description": "A beautiful waterfall cascading down a rocky cliff.",
        "npcs": traveling_party + ["a kingfisher", "a dragon"],
        "items": [],
        "vehicles": []
        },
    "a hidden grotto": {
        "exits": { "left" : "dark cave", "right": "a secret meadow" },
        "description": "A hidden grotto with sparkling crystals and a small pool of water.",
        "npcs": traveling_party + ["a fairy", "a unicorn"],
        "items": ["magic wand", "crystal ball" ],
        "vehicles": []
        },
    "a mountain pass": {
        "exits": { "left" : "a snowy peak", "right": "a tunnel" },
        "description": "A narrow mountain pass with steep cliffs on either side.",
        "npcs": traveling_party + ["a mountain goat", "an eagle"],
        "items": [],
        "vehicles": []
        },
    "a rainbow pool": {
        "exits": { "left" : "a waterfall", "right": "a crystal cave" },
        "description": "A pool of water that shimmers with all the colors of the rainbow.",
        "npcs": traveling_party + ["a seal"],
        "items": [],
        "vehicles": []
        },
    "a secret meadow": {
        "exits": { "left" : "a hidden grotto", "right": "a flower field" },
        "description": "A secret meadow filled with colorful wildflowers and tall grass.",
        "npcs": traveling_party + ["a butterfly", "a grasshopper"],
        "items": ["basket", "blanket" ],
        "vehicles": []
        },
    "a snowy peak": {
        "exits": { "left" : "a cliff face", "right": "a mountain pass"},
        "description": "A snowy peak with a breathtaking view of the surrounding mountains.",
        "npcs": traveling_party + ["a goat"],
        "items": ["coat", "boots" ],
        "vehicles": []
        },
    "a crystal cave": {
        "exits": { "left" : "a rainbow pool", "right": "a glittering chamber" },
        "description": "A cave filled with glittering crystals that reflect the light.",
        "npcs": traveling_party + ["a glowing book", "a shining scroll"],
        "items": ["crystal shard", "gemstone" ],
        "vehicles": []
        },
    "a flower field": {
        "exits": { "left" : "a secret meadow", "right": "large building" },
        "description": "A vast field filled with colorful flowers of all kinds.",
        "npcs": traveling_party + ["a bee", "a ladybug"],
        "items": ["dandelion", "notebook" ],
        "vehicles": []
        },
    "a cliff face": {
        "exits": { "right" : "a snowy peak"},
        "description": "A steep cliff face with jagged rocks and a sheer drop to the valley below.",
        "npcs": traveling_party + ["a hawk"],
        "items": ["gear", "helmet" ],
        "vehicles": []
        },
    "a glittering chamber": {
        "exits": { "left" : "a crystal cave" },
        "description": "A chamber filled with glittering treasures and precious gems.",
        "npcs": traveling_party + ["a treasure chest", "a golden crown"],
        "items": ["gold coins", "jewels" ],
        "vehicles": []
        },
    "large building": {
        "exits": { "left" : "a flower field" },
        "description": "A large building with tall pillars and a grand entrance.",
        "npcs": traveling_party + ["a guard", "a receptionist"],
        "items": ["keycard", "map" ],
        "vehicles": []
    },
}

# print header and welcome message
def print_welcome():
    print(80*"=")
    print(18*" " + "Welcome to the Fellowship of the Onion Ring!")
    print(80*"=")
    print("\n")

def get_player_name() -> str:
    name = input("What's your name? ")
    return name if name != "" else "Dingus"

def initial_dialog(player_name: str):
    #initial dialog with boss
    print(33*" " + "\\(0 0)/")
    print(33*" " + "  .|.")
    print(33*" " + "   O")
    print(33*" " + "   -")
    print(f"\n{player_name}! Are you daydreaming again? We have to get those onion rings, \nwe're running low. Did you hear a word I said?\n") 
    response = input("Possible responses are: (cry, no, yes) ")
    
    if response == "cry":
        print(f"You break down in tears. Your boss hands you a handkerchief to wipe your eyes, \nthen yells at you 'Get out to the truck!'")
        player_inventory.append("handkerchief")
    elif response == "no":
        print(f"Your boss rolls his eyes and yells 'Get out to the truck!'")
    elif response == "yes":
        print(f"Boss: Great! Now get to the truck")
    else:
        print(f"Your boss sighs. I'm too old for this.")
    print(80*"-")
    input("Press Enter to continue...")
    clear_screen()
    
def print_location():
    print(80*"-")
    print(f"You are at {player_location}.")
    print(locations[player_location]["description"])
    print(5*"=")
    if locations[player_location]["npcs"]:
         print(f"(0 0) You see: {', '.join(locations[player_location]['npcs'])}")
         print("  ^")
         print(" \\-/\n")	
    if locations[player_location]["vehicles"]:
         print(f"You notice the following vehicles: {', '.join(locations[player_location]['vehicles'])}\n")
    if locations[player_location]["items"]:
         print(f"You notice the following items: {', '.join(locations[player_location]['items'])}\n")
    print("------> Exits: " + ", ".join(locations[player_location]["exits"].keys()))
    print(5*"\n")

# display player inventory as a list
def show_inventory():
    print(f"You have: {", ".join(player_inventory)}")
    print("\n")

# clear screen
def clear_screen():
    print(25*"\n")

def talk(player_location: str, npc: str):  
    global locations
    if npc == "":   
        talk_to = ", ".join(locations[player_location]["npcs"])
        npc = input("Who do you want to talk to? (" + talk_to + ") ")

    if npc.capitalize() in coworkers:
        npc = npc.capitalize()

    if npc in locations[player_location]["npcs"]:
            print(f"You talk to {npc}. They greet you warmly.\n")
    else:
        print(f"There is no {npc} here.\n")

def take(player_location: str, item: str):
    global player_inventory
    if item == "":
        item = input("What do you want to take? ")
    if item in locations[player_location]["items"]:
        player_inventory.append(item)
        locations[player_location]["items"].remove(item)
        print(f"You take the {item}.\n")
    else:
        print(f"There is no {item} here to take.\n")

def drop(player_location: str, item: str):
    global player_inventory
    if item == "":
        item = input("What do you want to drop? ")
    if item in player_inventory:
        player_inventory.remove(item)
        locations[player_location]["items"].append(item)
        print(f"You drop the {item}.\n")
    else:
        print(f"You don't have a {item} to drop.\n")

def use(player_location: str, item: str):
    global player_inventory
    if item == "":
        item = input("What do you want to use? ")
    if item in player_inventory:
        print(f"You use the {item}.\n")
    else:
        print(f"You don't have {item}.\n")
    
def drive(player_location: str, vehicle: str):
    global current_vehicle
    if vehicle == "":
        vehicle = input("What vehicle do you want to drive? ")
    if vehicles[vehicle]["uses"] != "drive":
        print(f"You must drive this vehicle.\n")
        return
    if vehicle in locations[player_location]["vehicles"]:
        current_vehicle = vehicle
        locations[player_location]["vehicles"].remove(vehicle)
        print(f"You get into the {vehicle}.\n")
    else:
        print(f"There is no {vehicle} here to drive.\n")

def ride_vehicle(player_location: str, vehicle: str):
    global current_vehicle
    if vehicle == "":
        vehicle = input("What vehicle do you want to ride? ")
    current_vehicle = vehicle
    if vehicles[vehicle]["uses"] != "ride":
        print(f"You must ride the .\n")
        return
    if vehicle in locations[player_location]["vehicles"]:
        current_vehicle = vehicle
        locations[player_location]["vehicles"].remove(vehicle)
        print(f"You get on the {vehicle}.\n")
    else:
        print(f"There is no {vehicle} here to drive.\n")

def start_vehicle(player_inventory: list, vehicle: str):
    global current_vehicle

    if vehicle == "":
        vehicle = input("What vehicle do you want to start? ")

    keys = vehicle + "_keys"
    if keys not in player_inventory:
        print(f"You don't have the keys to start the {vehicle}.\n")
        return
    if vehicle == current_vehicle:
        if not vehicles[vehicle]["started"]:
            vehicles[vehicle]["started"] = True
            print(f"You use the {vehicle} keys to start the {vehicle}.\n")
        else:
            print(f"The {vehicle} is already started.\n")
    else:
        print(f"You must {vehicles[vehicle]['uses']} the {vehicle} before starting it.\n")

def exit_vehicle(player_location: str, vehicle: str):   
    global current_vehicle
    if vehicle == "":
        vehicle = input("What vehicle do you want to exit? ")
    if vehicle == current_vehicle:
        locations[player_location]["vehicles"].append(vehicle)
        current_vehicle = None
        print(f"You exit the {vehicle}.\n")
    else:
        print(f"You are not in the {vehicle}.\n")

def handle_vehicle_movement(current_location: str, direction: str):
    global player_location
    global vehicles
    global current_vehicle

    if vehicles[current_vehicle]["started"]:
        if vehicles[current_vehicle]["fuel"] > 0:
            new_location = locations[current_location]["exits"][direction]
            player_location = new_location
            vehicles[current_vehicle]["fuel"] -= vehicles[current_vehicle]["rate"]  # Decrease fuel by rate units per move
            if vehicles[current_vehicle]["rate"] == 0:
                print(f"You {vehicles[current_vehicle]['uses']} the {current_vehicle} {direction} to {new_location}.")
            else:
                print(f"You {vehicles[current_vehicle]['uses']} the {current_vehicle} {direction} to {new_location}. Fuel left: {vehicles[current_vehicle]['fuel']}.\n")
        else:
            print(f"The {current_vehicle} is out of fuel! You need to refuel before moving.\n")
    else:
        print(f"The {current_vehicle} is not started! You need to start it before moving.\n")

def move(current_location: str, direction: str):
    global player_location
    global locations
    global current_vehicle

    if direction in locations[current_location]["exits"]:
        # Handle vehicle movement if in a vehicle
        # Move the player to the new location
        if current_vehicle:
            handle_vehicle_movement(current_location, direction)
        else:
            player_location = locations[current_location]["exits"][direction]
            print(f"You move {direction} to {player_location}.\n")
    else:
        print("You can't go that way.\n")

def handle_input():
    global player_location
    global game_running

    # Parse the player's input. The input can be 'move [direction]', 'talk [target]', 'inventory', or 'quit'.
    # target is used for the npc name when talking
    # target is also used to store the direction for move command
    user_input = input("What do you want to do? (move [direction], talk [target], inventory, quit) ")
    command_list = user_input.strip().lower().split()

    #Check for empty input
    if len(command_list) == 0:
        print("Please enter a command. 'help' shows available commands.\n")
        return game_running
    
    # Grab the command
    command = command_list[0]

    # set target for talk and move commands
    target = command_list[1] if len(command_list) > 1 else ""
    
    clear_screen()
    
    if command == "move":
        move(player_location, target)
    elif command == "talk":
        talk(player_location, target)
    elif command == "take":
        take(player_location, target)
    elif command == "drop":
        drop(player_location, target)
    elif command == "use":
        use(player_location, target)
    elif command == "drive":
        drive(player_location, target)
    elif command == "ride":
        ride_vehicle(player_location, target)
    elif command == "start":
        start_vehicle(player_inventory, target)
    elif command == "exit":
        exit_vehicle(player_location, target)
    elif command == "inventory":
        show_inventory()
    elif command == "help":
        print("Available commands: move [direction], talk [target], take [item], drop [item],\nuse [item], inventory, quit\n")
    elif command == "quit" or command == "q":
        print("Thanks for playing the Fellowship of the Onion Ring!")
        game_running = False
    else:
        print("Invalid command. Please try again.\n")
    
    return game_running



# main game loop
def main(): 
    global player_location
    global game_running
    global locations
    global player_inventory
    global current_vehicle
    

    #Display the welcome info
    print_welcome()

    #ask for player name and start dialog
    player_name = get_player_name()

    initial_dialog(player_name)

    # Start at Hobbs Hamburgers
    player_location = "Hobbs Hamburgers"

    print("There are {locations_count} locations to explore in this game.".format(locations_count=len(locations)))

    # Game logic loop
    while game_running:
        print_location()
        game_running = handle_input()

if __name__ == "__main__":
    main()
