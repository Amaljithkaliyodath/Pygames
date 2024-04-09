import sys

# Define the game variables
current_room = 0
rooms = {
    0: {
        "name": "Starting Room",
        "description": "You are in a small room with doors to the north and east.",
        "exits": {"north": 1, "east": 2},
    },
    1: {
        "name": "North Room",
        "description": "You are in a dimly lit room with a door to the south.",
        "exits": {"south": 0},
    },
    2: {
        "name": "East Room",
        "description": "You are in a small room with a door to the west.",
        "exits": {"west": 0},
    },
}

# Define the game loop
while True:
    # Print the current room description
    print(rooms[current_room]["description"])

    # Get the user's input
    action = input("What do you want to do? ").lower().split()

    # Check if the user wants to quit
    if len(action) == 1 and action[0] == "quit":
        sys.exit(0)

    # Check if the user wants to move
    if len(action) == 1 and action[0] in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][action[0]]
    elif len(action) == 2 and action[0] == "go" and action[1] in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][action[1]]
    else:
        print("I don't understand that command.")

    # Print the current room name
    print("You are in the", rooms[current_room]["name"])