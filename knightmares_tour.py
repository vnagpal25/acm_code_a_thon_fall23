"""
My solution to 'Knightmare's Tour? Never again'
"""
import random

def opp(num):
    """Used to decrement delta x and delta y"""
    if num > 0:
        return -1
    elif num < 0:
        return 1
    else:
        return 0


def sign(num):
    """Used to move in the direction of delta x and delta y"""
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


def get_all_squares_with_num(board, num):
    """Returns all squares on the board that have a certain number"""
    all_indices = []
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == num:
                all_indices.append((i, j))
    return all_indices


def failed_move(index, delta, upper_limit, lower_limit=0):
  """Checks if an index is out of bounds, if so an illegal move was performed"""
  return (index + sign(delta) < lower_limit) or (index + sign(delta) > (upper_limit - 1))    


def move(board, delta_x, delta_y, upper_limit, to_explore, horizontal):
  """Performs either move in x or y direction, and returns updated state variables"""
  
  # continue stepping in the direction of delta x until we hit a boundary or we have successfully moved (delta x or delta_y = 0)
  delta = delta_x if horizontal else delta_y

  while abs(delta) > 0 and j + sign(delta) >= 0 and j + sign(delta) <= (upper_limit-1):
      #moved across board
      i, j = i, j + sign(delta)
      
      # number of new square
      new_square = board[i][j]

       # if we have already seen it ignore it
      if new_square == curr_square:
          continue
      else:
          # only update delta x if we reached a new square
          delta += opp(delta)

          # next move
          next_move = (delta, delta_y) if horizontal else (delta_x, delta)

          # now get all the indices that have that same number
          all_i_j = get_all_squares_with_num(board, new_square)

          # from all of these indices we need to explore delta_y, delta_x away from this square
          for pos in all_i_j:
              if (pos[0], pos[1]) != (i, j):
                  to_explore[(pos[0], pos[1])] = next_move          
          
          # mark the new square as current square
          curr_square = new_square
  
  # updating for returning
  delta_x = delta if horizontal else delta_x
  delta_y = delta if not horizontal else delta_y

  # return necessary variables
  return i, j, delta_x, delta_y, curr_square, to_explore


def move_x_then_y(board, i, j, move):   
    """Moves in the x direction first, then the y direction"""
    
    # m x n board
    m, n = len(board), len(board[0])
    
    # to return will contain the unique squares that we can reach with this move
    possible_squares = set()
    
    # get the delta x and delta y
    delta_x, delta_y = move
    
    # delta y corresponds to change in row number (i) delta x corresponds to change in column number (j)

    # map i, j to delta_x, delta_y
    # when exploring we might come across squares that are part of bigger tiles. There may be multiple tiles that we can reach from here.
    # keeps track of which tile we landed on, and how much to move from there
    to_explore = {(i, j):(delta_y, delta_x)}
    
    # keep exploring until the move is exhausted
    while to_explore:
        # pick random key to explore
        (i, j) = random.choice(list(to_explore))
        
        # square number where we are at
        curr_square = board[i][j]
                
        # from here we need to move this much, pop the node because no need to explore again
        (delta_y, delta_x) = to_explore.pop((i, j))

       # move in the x direction 
        _, j, delta_x, _, curr_square, to_explore = move(board, delta_x, delta_y, n, to_explore, True)
       
        # if we reached a boundary, we failed to move. no need to explore further
        if failed_move(j, delta_x, n):
            continue
        
        # move in the y_direction
        i, _, _, delta_y, curr_square, to_explore = move(board, delta_x, delta_y, m, to_explore, False)

        # if we reached a boundary, we failed to move. no need to explore further
        if failed_move(i, delta_y, m):
            continue

        possible_squares.add(curr_square)

    # return unique squares
    return possible_squares


def move_y_then_x(board, i, j, move):
    """Moves in the y direction first, then the x direction"""
    
    # m x n board
    m, n = len(board), len(board[0])
    
    # to return will contain the unique squares that we can reach with this move
    possible_squares = set()
    
    # get the delta x and delta y
    delta_x, delta_y = move
    
    # delta y corresponds to change in row number (i) delta x corresponds to change in column number (j)
    # map i, j to delta_x, delta_y
    # when exploring we might come across squares that are part of bigger tiles. There may be multiple tiles that we can reach from here.
    # keeps track of which tile we landed on, and how much to move from there
    to_explore = {(i, j):(delta_y, delta_x)}
    
    # keep exploring until the move is exhausted
    while to_explore:
        # pick random key to explore
        (i, j) = random.choice(list(to_explore))
        
        # square number where we are at
        curr_square = board[i][j]
                
        # from here we need to move this much, pop the node because no need to explore again
        (delta_y, delta_x) = to_explore.pop((i, j))

        # move in the y_direction
        i, _, _, delta_y, curr_square, to_explore = move(board, delta_x, delta_y, m, to_explore, False)

        # if we reached a boundary, we failed to move. no need to explore further
        if failed_move(i, delta_y, m):
            continue

       # move in the x direction 
        _, j, delta_x, _, curr_square, to_explore = move(board, delta_x, delta_y, n, to_explore, True)
       
        # if we reached a boundary, we failed to move. no need to explore further
        if failed_move(j, delta_x, n):
            continue

        possible_squares.add(curr_square)

    # return unique squares
    return possible_squares

    
def solve(board, y_pos, x_pos):
    """
    Returns the number of unique squares that can be reached in one knight's move
    """
    
    # get all possible squares where the knight could be sitting (all squares with the same number)
    curr_num = board[y_pos][x_pos]
    all_starting_positions = get_all_squares_with_num(board, curr_num)
    
    #hash set that keeps track of numbers reached, we are just going to count the number of elements in here at the end
    reached_squares = set()

    # all possible move that a knight can make
    valid_moves = [(1, 2), (2, 1), (2, -1), (1, -2), 
               (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

    # from each of the possible starting positions
    for starting_pos in all_starting_positions:
        # with each of the following moves
        for move in valid_moves:
            # get position
            i, j = starting_pos
            
            # Use of union operation of sets 'extends' the set of unique squares

            # first move vertically then horizontally
            reached_squares = reached_squares | move_y_then_x(board, i, j, move)
            
            # first move horizontally then vertically
            reached_squares = reached_squares | move_x_then_y(board, i, j, move)
            
    # returns the number of unique squares            
    return len(reached_squares)


def get_board():
    """Gets the board from input"""
    num_rows, num_cols, y_pos, x_pos = tuple(map(int, input().split()))
    
    board = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    for i in range(num_rows):
        row = tuple(map(int, input().split()))
        for j, num in enumerate(row):
            board[i][j] = num
    return board, y_pos, x_pos

  
def main():
    """Main Function"""
    # getting number of test cases
    num_test_cases = int(input())
    
    # solving for each different test case
    for _ in range(num_test_cases):
        # get the board and the position of the knight
        board, y_pos, x_pos = get_board()
        
        # solve!
        num_unique_moves = solve(board, y_pos, x_pos)
        
        # print solution
        print(num_unique_moves)
    
    
if __name__=='__main__':
    main()
