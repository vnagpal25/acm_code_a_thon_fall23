"""
My solution to 'Haunted House'
Utilizes Dynamic Programming
"""

def read_input():
    """Reads the user input"""
    m, n = map(int, input().split())
    matrix = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        row = tuple(map(int, input().split()))
        for j in range(n):
            matrix[i][j] = row[j]

    return m, n, matrix


def main():
    """Main Function"""

    # get input
    m, n, matrix = read_input()

    # initialize need matrix
    # the (i, j) entry of this matrix contains the minimum amount of candies need to survive the square
    need_matrix = [[0 for i in range(n)] for j in range(m)]

    # how much we need to get to the last square
    
    # if there is a non-negative number in the last square, we only need 1 candy going in
    # however, if it is negative, we need at least (1 - penalty) going in to endure that penalty and survive
    need_matrix[-1][-1] = max(1, 1 - matrix[-1][-1])

    # fill in last column, going from the bottom up
    # utilizing same logic as before, if the haunted house square has more than what we need for the next square, we will only need 1 going into that square
    # other wise we will need (min_needed for next square - penalty) to endure this penalty
    for i in range(m - 2, -1, -1):
        need_matrix[i][-1] = max(1, need_matrix[i+1][-1] - matrix[i][-1])

    # fill in the last row, going from right to left
    # utilizing the same logic as before
    for i in range(n - 2, -1, -1):
        need_matrix[-1][i] = max(1, need_matrix[-1][i+1] - matrix[-1][i])

    # fill out the rows from top to bottom
    for i in range(m - 2, -1, -1):
        # fill out the columns from right to left
        for j in range(n - 2, -1, -1):
            # only care about the minimum cost of one path, because this ensures optimality
            # so we will always choose the path that requires less candy
            min_needed_to_progress = min(need_matrix[i+1][j], need_matrix[i][j+1])

            # same logic as before
            # if the square has more than what we need for one of the next squares, we only need 1 going in
            # otherwise we need (min_needed for next square - penalty) to endure this penalty
            need_matrix[i][j] = max(1, min_needed_to_progress - matrix[i][j])

    # once we have filled out the need matrix, we can just print the first square.
    # this first element is the minimum amount of candies needed to walk through the entire maze and exit with at least 1 candy remaining
    print(need_matrix[0][0])


if __name__ == '__main__':
    main()
