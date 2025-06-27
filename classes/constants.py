# Grid Settings
# Define the number of rows and columns in the grid
# Define the padding between cells in the grid
# Define the total size (width and height) of the game window
GRID_LEN = 4
GRID_PADDING = 10
SIZE = 400
# Color and Font Settings
# Background color of the game window
# Background color for empty grid cells
BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
# Background colors for each tile value
BACKGROUND_COLOR_DICT = {
    2: "#eee4da",       # Light beige
    4: "#ede0c8",       # Slightly darker beige
    8: "#f2b179",       # Light orange
    16: "#f59563",      # Deeper orange
    32: "#f67c5f",      # Reddish orange
    64: "#f65e3b",      # Bright red-orange
    128: "#edcf72",     # Yellowish
    256: "#edcc61",     # Golden yellow
    512: "#edc850",     # Yellow gold
    1024: "#edc53f",    # Gold
    2048: "#edc22e",    # Deep gold
}
# Foreground (text) colors for each tile value
FOREGROUND_COLOR_DICT = {
    2: "#776e65",       # Dark brown
    4: "#776e65",       # Same as for 2
    8: "#f9f6f2",       # Off-white
    16: "#f9f6f2",      # Off-white
    32: "#f9f6f2",      # Off-white
    64: "#f9f6f2",      # Off-white
    128: "#f9f6f2",     # Off-white
    256: "#f9f6f2",     # Off-white
    512: "#f9f6f2",     # Off-white
    1024: "#f9f6f2",    # Off-white
    2048: "#f9f6f2",    # Off-white
}
# Font used for displaying tile numbers (font family, size, style)
FONT = ("Verdana", 40, "bold")