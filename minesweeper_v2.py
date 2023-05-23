# This program takes a grid of '#' and '-' (where each hash represent a mine and each dash represents a mine-free spot) and then uses a 
# function to return a new grid where each dash is replaced by a digit. This digit indicates the number of mines immediately adjacent
#   to that spot in every direction (that is horizontally, vertically and diagonally). 

# Define the function with the input grid as paramenter:
def minesweeper (input_grid):

    # Create two variables to identifiy the dimensions of the grid:
    num_rows = len(input_grid)
    num_coloumns = len(input_grid[0])
    # Create a new empty grid with the same dimensions as the input grid. 
    final_grid = [[None for a in range(num_coloumns)] for b in range(num_rows)]

    # Now, with a 'for loop', look through every row and every column:
    for x in range(num_rows):
        for y in range(num_coloumns):
            
            # Using an 'if else' structure, tell Python to copy the hashes into the new grid and then explain what to do with the dashes.
            if input_grid[x][y] == '#':
                final_grid[x][y] = '#'
            else:
                # create variable to count the adjacent mines.
                adjacent_mines = 0
                # using a nested 'for loop', define the range of adjacent cells so we can look for the hashes and finally add the mines to the counting variable (credit to https://www.youtube.com/watch?v=lla6QlAF4HQ&list=PLhvY7DW0yVJTckDs-lK-qHcJlWh_iKybP&index=4&t=741s&pp=gAQBiAQB).
                for r in range(x-1, x+2):       # x-1 is the row above. x+2 is the "range stop position" which is not included (therefore stops at x+1 which is the row below)
                    for c in range(y-1, y+2):   # left column and right column 
                        # using a nested 'if' sentence, define the grid boundaries and look for the hashes.
                        if r>=0 and r <= num_rows-1 and c >=0 and c <= num_coloumns-1 and input_grid[r][c] == '#':
                            adjacent_mines +=1
                # Add the number of adjacent mines to the new grid by converting them to string (since the new grid contains hashes and numbers)
                final_grid[x][y] = str(adjacent_mines)
    
    # Finally, print the new grid
    print("The final grid is:")
    for row in final_grid:
        print(row)

# This is the input grid:
input_grid = [  [ '-', '-', '-', '#', '#' ],
                [ '-', '#', '-', '-', '-' ],
                [ '-', '-', '#', '-', '-' ],
                [ '-', '#', '#', '-', '-' ],
                [ '-', '-', '-', '-', '-' ]   ]

print("The input grid is:")
for rows in input_grid:
    print (rows)

# Finally, call the function
minesweeper(input_grid)
