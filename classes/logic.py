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
    return new_board, moved 
# Track whether any merge occurred
# Loop through each row
# Loop through each tile except the last in the row
# Check if adjacent tiles are equal and non-zero
# Merge tiles by doubling the value
# Set the merged tile to zero
# Mark as merged
def merge(board):
    merged = False
    for row_index in range(GRID_SIZE):
        for column_index in range(GRID_SIZE - 1):
            if board[row_index][column_index] == board[row_index][column_index + 1] and board[row_index][column_index] != 0:
                board[row_index][column_index] *= 2
                board[row_index][column_index + 1] = 0
                merged = True
# Return the updated board and merge status
    return board, merged
# Reverse each row (used for right move)
def reverse(board):
    return [row[::-1] for row in board]
# Transpose the matrix (used for up/down moves)
def transpose(board):
    return [list(row) for row in zip(*board)]
# First compress the tiles to the left
# Then merge adjacent equal tiles
# Compress again to shift after merging
# Return the final board and whether a move occurred
def move_left(board):
    compressed_board, did_compress = compress(board)
    merged_board, did_merge = merge(compressed_board)
    final_board, _ = compress(merged_board)
    return final_board, did_compress or did_merge
# Reverse the board to reuse left logic
# Perform left move on reversed board
# Reverse back and return result
def move_right(board):
    reversed_board = reverse(board)
    moved_board, moved = move_left(reversed_board)
    return reverse(moved_board), moved
# Transpose to reuse left move logic
# Perform left move on transposed board
# Transpose back and return result
def move_up(board):
    transposed_board = transpose(board)
    moved_board, moved = move_left(transposed_board)
    return transpose(moved_board), moved
# Transpose the board
# Perform right move on transposed board
# Transpose back and return result
def move_down(board):
    transposed_board = transpose(board)
    moved_board, moved = move_right(transposed_board)
    return transpose(moved_board), moved
# Check for any empty cell in the board
# Game is not over if at least one empty cell exists
def check_game_over(board):
    for row in board:
        if 0 in row:
            return False
# Check for possible horizontal merges
# Game is not over if adjacent horizontal tiles can merge
    for row_index in range(GRID_SIZE):
        for column_index in range(GRID_SIZE - 1):
            if board[row_index][column_index] == board[row_index][column_index + 1]:
                return False
# Check for possible vertical merges
# Game is not over if adjacent vertical tiles can merge
    for column_index in range(GRID_SIZE):
        for row_index in range(GRID_SIZE - 1):
            if board[row_index][column_index] == board[row_index + 1][column_index]:
                return False
# No moves left; game is over
    return True