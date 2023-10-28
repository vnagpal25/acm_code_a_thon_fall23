"""
My solution to 'Harry the Hexagon Hacker'
"""

# these are the valid moves that you can make within a hexagonal grid
# the coordinate system allows for accurately mapping the path within a hexagon
valid_moves = {"NW":(-0.5, 0.5), "N":(0, 1), "NE":(0.5, 0.5), "SE":(0.5, -0.5), "S":(0, -1), "SW":(-0.5, -0.5)}

# these are not legal moves in a hexagonal grid
to_skip = {"E", "W"}


def parse_directions(directions):
    """Parses the Input Directions and returns them as a list"""
    # to return
    move_order = []

    # iterates over the characters
    for i, char in enumerate(directions):
        # illegal move skip
        if char in to_skip:
            continue
        
        # Checks for NW, NE, SW, SE
        elif i < len(directions) - 1 and char in valid_moves and directions[i+1] in to_skip:
            move = char+directions[i+1]
            move_order.append(move)
        
        # Checks for N, S
        elif char in valid_moves:
            move_order.append(char)

    # returns the moves
    return move_order


def get_num_mult_tiles(hex_grid_visited):
    """
    Given a hashmap of the grid coordinates that maps to the number of times each tile was visited
    Returns the number of tiles that were visited more than once
    """
    num = 0
    for _, times_visited in hex_grid_visited.items():
        if times_visited > 1:
            num += 1
    return num


def main():
    """Main Function"""
    
    # gets input
    num_test_cases = int(input())
    
    # iterates over test cases
    for _ in range(num_test_cases):
        # represents the initial hexagon we are located in (origin)
        curr_hex = (0, 0)

        # hashmap maps coordinates to number of times visited
        # we have already visited the initial square once, by virtue of being there
        hex_grid_visited = {(0, 0): 1} 

        # gets n and the directions
        n,  directions = input().split()
        n = int(n)
        
        # parse the direction string
        move_order = parse_directions(directions)

        # peforms each move and updates the hashmap
        for move in move_order:
            # gets amount that we need to move
            delta_d = valid_moves[move]
            
            # calculate new current square
            curr_hex = tuple(x1+x2 for x1, x2 in zip(curr_hex, delta_d))
            
            # updates hashmap
            hex_grid_visited[curr_hex] = hex_grid_visited.get(curr_hex, 0) + 1
        
        # get number of tiles visited more than once
        x = get_num_mult_tiles(hex_grid_visited)
        
        # print yes if non zero and divides n, else no
        if x > 0 and x % n == 0:
            print(f'yes {x}')
        else:
            print(f'no')
    

if __name__=='__main__':
    main()
