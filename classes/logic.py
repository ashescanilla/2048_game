# Import the random module to generate random numbers
import random
# Define the size of the 2048 game board (4x4 grid)
GRID_SIZE = 4
# Create and return a 4x4 grid initialized with zeros
def start_game():
    return [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
# Randomly select a row index
# Randomly select a column index
def add_new_tile(board):
    row_index = random.randint(0, GRID_SIZE - 1)
    column_index = random.randint(0, GRID_SIZE - 1)
# Keep generating until an empty cell is found
# Retry row
# Retry column
    while board[row_index][column_index] != 0:
        row_index = random.randint(0, GRID_SIZE - 1)
        column_index = random.randint(0, GRID_SIZE - 1)
# Place a new tile (value 2) at the selected empty cell
    board[row_index][column_index] = 2
# Initialize a new empty board
# Track whether any tile was moved
def compress(board):
    new_board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    moved = False
# Loop through each row
# Position to place the next non-zero tile
# Loop through each column in the row
# If the tile is not empty
# Move tile to the leftmost available position
# Check if the tile actually moved
# Mark as moved
# Increment the position for the next tile
    for row_index in range(GRID_SIZE):
        position = 0
        for column_index in range(GRID_SIZE):
            if board[row_index][column_index] != 0:
                new_board[row_index][position] = board[row_index][column_index]
                if column_index != position:
                    moved = True
                position += 1
# Return the new board and move status

# Track whether any merge occurred
# Loop through each row
# Loop through each tile except the last in the row
# Check if adjacent tiles are equal and non-zero
# Merge tiles by doubling the value
# Set the merged tile to zero
# Mark as merged

# Return the updated board and merge status

# Reverse each row (used for right move)

# Transpose the matrix (used for up/down moves)

# First compress the tiles to the left
# Then merge adjacent equal tiles
# Compress again to shift after merging
# Return the final board and whether a move occurred

# Reverse the board to reuse left logic
# Perform left move on reversed board
# Reverse back and return result

# Transpose to reuse left move logic
# Perform left move on transposed board
# Transpose back and return result

# Transpose the board
# Perform right move on transposed board
# Transpose back and return result

# Check for any empty cell in the board
# Game is not over if at least one empty cell exists

# Check for possible horizontal merges
# Game is not over if adjacent horizontal tiles can merge

# Check for possible vertical merges
# Game is not over if adjacent vertical tiles can merge

# No moves left; game is over