import time

# Define the rooms and their descriptions
rooms = {
    'entrance': "You are at the entrance of a mysterious dungeon.",
    'hallway': "You find yourself in a dimly lit hallway.",
    'treasure_room': "You have entered the treasure room! Riches beyond imagination await...",
    'monster_room': "You have entered a room with a fearsome monster! Choose your next move...",
    'exit': "You have found the exit! Congratulations, you've made it out alive!"
}

# Define the game's logic
def game():
    current_room = 'entrance'
    while current_room != 'exit':
        print(rooms[current_room])
        time.sleep(1)
        
        if current_room == 'entrance':
            print("Options: 1 - Enter the dungeon, 2 - Leave")
            choice = input("What will you do? ")
            if choice == '1':
                current_room = 'hallway'
            elif choice == '2':
                print("You have chosen to leave the dungeon.")
                break
            else:
                print("Invalid choice!")
        
        elif current_room == 'hallway':
            print("Options: 1 - Go to the treasure room, 2 - Enter the monster room, 3 - Go back")
            choice = input("What will you do? ")
            if choice == '1':
                current_room = 'treasure_room'
            elif choice == '2':
                current_room = 'monster_room'
            elif choice == '3':
                current_room = 'entrance'
            else:
                print("Invalid choice!")
        
        elif current_room == 'treasure_room':
            print("Congratulations! You've found the treasure!")
            current_room = 'exit'
        
        elif current_room == 'monster_room':
            print("A fearsome monster blocks your way!")
            print("Options: 1 - Fight, 2 - Flee")
            choice = input("What will you do? ")
            if choice == '1':
                print("You bravely fought the monster, but it was too strong...")
                print("Game Over!")
                break
            elif choice == '2':
                print("You wisely chose to flee back to the hallway.")
                current_room = 'hallway'
            else:
                print("Invalid choice!")

# Start the game
print("Welcome to Mysterious Dungeon!")
game()
print("Thank you for playing!")

