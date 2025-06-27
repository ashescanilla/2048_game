# Import Tkinter widgets and alignment constant
from tkinter import Frame, Label, CENTER 
# Import random module for generating random positions
import random
# Import the custom logic module for game functions
import logic 
# Import constants for game settings and styling
import constants as constants_module 
def generate_random_position():
# Generate a random index within grid bounds
    return random.randint(0, constants_module.GRID_LEN - 1) 
# Define the main GameGrid class inheriting from Tkinter Frame
# Initialize the game window
# Initialize the parent Frame class
class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)
# Use grid geometry manager to organize widgets
# Set the window title to "2048"
# Bind keyboard input to key_down_handler method
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down_handler)
# Map movement keys to their corresponding logic functions
        self.commands = {
            'Up': logic.move_up,
            'Down': logic.move_down,
            'Left': logic.move_left,
            'Right': logic.move_right
        }
# Initialize an empty list to hold the grid's label widgets
# Call method to create visual grid
# Call method to initialize the game matrix
# Call method to update the grid UI with values
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
# Start the Tkinter main event loop
        self.mainloop() 
# Set up the visual grid interface
# Create the background frame
# Place the background frame on the grid
    def init_grid(self):
        background = Frame(self, bg=constants_module.BACKGROUND_COLOR_GAME,
                           width=constants_module.SIZE, height=constants_module.SIZE)
        background.grid()
# Loop over each row index
# Create a new list to hold this row's labels
# Loop over each column index
# Create a cell frame
# Place the cell frame in the grid
# Create label for tile
# Place the label inside the cell
# Add the label to the row list
# Add the row to the grid_cells 2D list
        for row_index in range(constants_module.GRID_LEN):
            grid_row = []
            for column_index in range(constants_module.GRID_LEN):
                cell = Frame(background, bg=constants_module.BACKGROUND_COLOR_CELL_EMPTY,
                             width=constants_module.SIZE / constants_module.GRID_LEN,
                             height=constants_module.SIZE / constants_module.GRID_LEN)
                cell.grid(row=row_index, column=column_index, padx=constants_module.GRID_PADDING,
                          pady=constants_module.GRID_PADDING)
                label = Label(master=cell, text="", bg=constants_module.BACKGROUND_COLOR_CELL_EMPTY,
                              justify=CENTER, font=constants_module.FONT, width=4, height=2)
                label.grid()
                grid_row.append(label)
            self.grid_cells.append(grid_row)
# Initialize the game matrix with starting tiles
# Start with an empty matrix
# Add the first random tile
# Add the second random tile
    def init_matrix(self):
        self.matrix = logic.start_game()
        logic.add_new_tile(self.matrix)
        logic.add_new_tile(self.matrix)
# Update the visual tiles based on the matrix values
# Loop over each row
# Loop over each column
# Get the current tile value
# If the tile is empty
# Set to empty appearance
# If the tile has a number
# Show the number
# Set background color
# Set text color
# Refresh the UI to reflect updates
    def update_grid_cells(self):
        for row_index in range(constants_module.GRID_LEN):
            for column_index in range(constants_module.GRID_LEN):
                current_tile_value = self.matrix[row_index][column_index]
                if current_tile_value == 0:
                    self.grid_cells[row_index][column_index].configure(
                        text="", bg=constants_module.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[row_index][column_index].configure(
                        text=str(current_tile_value),
                        bg=constants_module.BACKGROUND_COLOR_DICT[current_tile_value],
                        fg=constants_module.FOREGROUND_COLOR_DICT[current_tile_value])
        self.update_idletasks()
# Handle keyboard key press
# Get the string name of the key pressed
# If the key is one of the valid commands
# Apply the move and get validity
# If the move was valid (tiles moved or merged)
# Add a new random tile to the board
# Update the visual tiles
# Check if no more moves are possible
# Show "Game Over" message
    def key_down_handler(self, event):
        user_key = event.keysym
        if user_key in self.commands:
            self.matrix, move_valid = self.commands[user_key](self.matrix)
            if move_valid:
                logic.add_new_tile(self.matrix)
                self.update_grid_cells()
                if logic.check_game_over(self.matrix):
                    self.game_over_display()
# Display a "Game Over" message on screen
# Create a frame for the message
# Center the frame in the window
# Create a label for "Game Over"
# Pack the label into the frame
