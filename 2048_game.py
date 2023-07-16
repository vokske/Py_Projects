import random
import pygame

grid_size = 4
grid = [[0] * grid_size for _ in range(grid_size)]

def print_grid():
    for row in grid:
        print(row)

print_grid()

# Function to initialize the grid with two random "2" tiles
def initialize_grid():
    grid = [[0] * 4 for _ in range(4)]
    add_random_tile(grid)
    add_random_tile(grid)
    return grid

# Function to add a random "2" tile to an empty cell in the grid
def add_random_tile(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[row][col] = 2

# Function to display the grid
def print_grid(grid):
    for row in grid:
        print(row)

# Function to check if there are any valid moves left
def has_valid_moves(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return True
            if j < 3 and (grid[i][j] == grid[i][j+1] or grid[j][i] == grid[j+1][i]):
                return True
    return False

# Initialize the grid
grid = initialize_grid()

# Function to display the grid using Pygame
def display_grid(grid):
    tile_size = 100
    screen.fill((255, 255, 255))  # Clear the screen

    for i in range(4):
        for j in range(4):
            tile_value = grid[i][j]
            tile_color = get_tile_color(tile_value)
            tile_rect = pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, tile_color, tile_rect)
            tile_text = font.render(str(tile_value), True, (0, 0, 0))
            text_rect = tile_text.get_rect(center=tile_rect.center)
            screen.blit(tile_text, text_rect)

    pygame.display.flip()

# Utility function to get tile color based on tile value
def get_tile_color(value):
    # Define colors based on tile values as per your preference
    colors = {
        0: (205, 193, 180),
        2: (238, 228, 218),
        4: (237, 224, 200),
        # ... Define colors for other tile values
    }
    return colors.get(value, (0, 0, 0))  # Default to black color for unknown values

# Function to handle the swipe to the left
def swipe_left(grid):
    for row in grid:
        # Shift all the tiles to the left
        shifted_row = []
        for tile in row:
            if tile != 0:
                shifted_row.append(tile)
        shifted_row += [0] * (4 - len(shifted_row))
        
        # Merge adjacent tiles
        for i in range(3):
            if shifted_row[i] == shifted_row[i + 1]:
                shifted_row[i] *= 2
                shifted_row[i + 1] = 0

        # Shift the merged tiles to the left
        shifted_row = [tile for tile in shifted_row if tile != 0] + [0] * (4 - len(shifted_row))
        
        # Update the grid row
        row[:] = shifted_row

def swipe_right(grid):
    for row in grid:
        # Shift all the tiles to the right
        shifted_row = []
        for tile in row:
            if tile != 0:
                shifted_row.insert(0, tile)
        shifted_row = [0] * (4 - len(shifted_row)) + shifted_row

        # Merge adjacent tiles
        for i in range(3, 0, -1):
            if shifted_row[i] == shifted_row[i - 1]:
                shifted_row[i] *= 2
                shifted_row[i - 1] = 0

        # Shift the merged tiles to the right
        shifted_row = [tile for tile in shifted_row if tile != 0] + [0] * (4 - len(shifted_row))

        # Update the grid row
        row[:] = shifted_row


# Function to handle the swipe upwards
def swipe_up(grid):
    for col in range(4):
        # Extract the column
        column = [grid[row][col] for row in range(4)]

        # Shift all the tiles upwards
        shifted_column = []
        for tile in column:
            if tile != 0:
                shifted_column.append(tile)
        shifted_column += [0] * (4 - len(shifted_column))

        # Merge adjacent tiles
        for i in range(3):
            if shifted_column[i] == shifted_column[i + 1]:
                shifted_column[i] *= 2
                shifted_column[i + 1] = 0

        # Shift the merged tiles upwards
        shifted_column = [tile for tile in shifted_column if tile != 0] + [0] * (4 - len(shifted_column))

        # Update the grid column
        for row in range(4):
            grid[row][col] = shifted_column[row]


# Function to handle the swipe downwards
def swipe_down(grid):
    for col in range(4):
        # Extract the column
        column = [grid[row][col] for row in range(4)]

        # Shift all the tiles downwards
        shifted_column = []
        for tile in column:
            if tile != 0:
                shifted_column.insert(0, tile)
        shifted_column = [0] * (4 - len(shifted_column)) + shifted_column

        # Merge adjacent tiles
        for i in range(3, 0, -1):
            if shifted_column[i] == shifted_column[i - 1]:
                shifted_column[i] *= 2
                shifted_column[i - 1] = 0

        # Shift the merged tiles downwards
        shifted_column = [tile for tile in shifted_column if tile != 0] + [0] * (4 - len(shifted_column))

        # Update the grid column
        for row in range(4):
            grid[row][col] = shifted_column[row]

# Initialize the grid
grid = initialize_grid()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
font = pygame.font.SysFont(None, 48)

# Display the initial grid

display_grid(grid)

# Main game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                swipe_left(grid)
                add_random_tile(grid)
                display_grid(grid)
            elif event.key == pygame.K_RIGHT:
                swipe_right(grid)
                add_random_tile(grid)
                display_grid(grid)
            elif event.key == pygame.K_UP:
                swipe_up(grid)
                add_random_tile(grid)
                display_grid(grid)
            elif event.key == pygame.K_DOWN:
                swipe_down(grid)
                add_random_tile(grid)
                display_grid(grid)

# Quit Pygame
pygame.quit()

