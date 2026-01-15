#Directions
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

#Printing words
DIR_NAMES = {
    NORTH: "(N)orth",
    SOUTH: "(S)outh",
    WEST:  "(W)est",
    EAST:  "(E)ast",
}

STARTING_TILE = 2,0

VALID_DIRECTIONS = {
    1: {EAST: 2, SOUTH: 4},
    2: {WEST: 1, EAST: 3},
    3: {WEST: 2, SOUTH: 6},
    4: {NORTH: 1, EAST: 5, SOUTH: 7},
    5: {WEST: 4, SOUTH: 8},
    6: {NORTH: 3, SOUTH: 9},
    7: {NORTH: 4},
    8: {NORTH: 5},
    9: {}
}

def move_player():
    #Makes the grid
    line1 = [1,2,3]
    line2 = [4,5,6]
    line3 = [7,8,9]
    grid_of_tiles = [line1,line2,line3]

    #Walls
    blocked_tiles = {
        (5,2),(2,5),
        (7,8),(8,7),
        (8,9),(9,8),
        (5,6), (6,5)
    }

    #Gives player a starting point
    player_row, player_col = STARTING_TILE

    #Variable to hold how many tries the player has done
    finish = 0

    while True:
        current_tile = grid_of_tiles[player_row][player_col]
        print(f"current location:{current_tile}")

        moves = VALID_DIRECTIONS[current_tile]

        #Input for the user
        direction = input("Direction: ").lower()

        #Takes the posititon of the player
        move_row, move_col = player_row, player_col

        #Moves player
        if direction == NORTH:
            move_row -= 1
        elif direction == SOUTH:
            move_row += 1
        elif direction == WEST:
            move_col -= 1
        elif direction == EAST:
            move_col += 1
        else:
            print("invalid move")
            continue

        #Checks if player is going outside
        if not (0 <= move_row < 3 and 0 <= move_col < 3):
            print("cant move outside dummy")
            continue

        #If it's safe then get position
        new_tile = grid_of_tiles[move_row][move_col]

        #Check if user is going to wall
        if (current_tile,new_tile) in blocked_tiles:
            print(f"cant go from {current_tile} to {new_tile}")
            continue

        #If all is good then continue
        player_row, player_col = move_row, move_col
        finish += 1

        # #After 200 tries the player fails.
        # if finish == 200:
        #     print("Too many tries")
        #     break

        #If player gets to the end of the box, he wins. 
        if new_tile == 9:
            print(grid_of_tiles[player_row][player_col])
            print("Victory!")
            break

#Starts the game
move_player()





# nums = []
# new_nums = []
# for i in range(1):
#     nums.append([])
#     for j in range(1, 10):
#         nums[i].append(j)
        
# for x in range(3):
#     new_nums.append(nums[i])
