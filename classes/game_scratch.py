import pygame
from classes.enemy import Enemy
from classes.player import Player
from classes.structures.doorBlock import doorBlock

# just a scratch
WALL = 1
DOOR = 2
grid = [[0] * 10 for _ in range(10)]
grid[0][1] = WALL
grid[1][2:6] = [WALL] * 4
grid[2][3] = DOOR

pygame.init()

#enemy = Enemy("demon", )
#player = Player()

#print("health:" + enemy._health)

door = doorBlock("first_door", "red", False)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Enemy catchs Player")

GRID_ROWS = 10  # Number of rows
GRID_COLS = 10  # Number of columns
CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS

GRID_COLOR = (200, 200, 200)  # Light gray
PLAYER_COLOR = (0, 250, 0)  # green
ENEMY_COLOR = (0, 0, 250)  # blue
WALL_COLOR = (250, 0, 0) # red
DOOR_COLOR = (200, 100, 200)
player_pos = [0, 0]  
enemy_pos = [9, 9]

def draw_grid():
    """Draw the 10x10 grid."""
    # Draw vertical lines
    for col in range(1, GRID_COLS):
        x = col * CELL_WIDTH
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))

    # Draw horizontal lines
    for row in range(1, GRID_ROWS):
        y = row * CELL_HEIGHT
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def draw_map():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):          
            x = col * CELL_WIDTH
            y = row * CELL_HEIGHT
            if [row, col] == player_pos:
                color = PLAYER_COLOR
            elif [row, col] == enemy_pos:
                color = ENEMY_COLOR
            elif grid[row][col] == WALL:
                color = WALL_COLOR
            elif grid[row][col] == DOOR:
                color = DOOR_COLOR
            else:
                continue  # Skip empty cells

            pygame.draw.rect(screen, color, (x, y, CELL_WIDTH, CELL_HEIGHT))

def draw_character(pos, col):
    """Draw the player as a rectangle in the grid."""
    x = pos[1] * CELL_WIDTH  
    y = pos[0] * CELL_HEIGHT
    pygame.draw.rect(screen, col, (x, y, CELL_WIDTH, CELL_HEIGHT))

def move_player(key):
    """Move the player on the grid based on the arrow keys."""
    if key == pygame.K_UP and player_pos[0] > 0 and grid[player_pos[0] - 1][player_pos[1]] != WALL:  # Move up
        player_pos[0] -= 1
    elif key == pygame.K_DOWN and player_pos[0] < GRID_ROWS - 1  and grid[player_pos[0] + 1][player_pos[1]] != WALL:  # Move down
        player_pos[0] += 1
    elif key == pygame.K_LEFT and player_pos[1] > 0 and grid[player_pos[0]][player_pos[1] - 1] != WALL:  # Move left
        player_pos[1] -= 1
    elif key == pygame.K_RIGHT and player_pos[1] < GRID_COLS - 1 and grid[player_pos[0]][player_pos[1] + 1] != WALL:  # Move right
        player_pos[1] += 1

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit if the close button is pressed
            running = False
        elif event.type == pygame.KEYDOWN:  # Handle arrow key presses
            move_player(event.key)

    screen.fill((0, 0, 0))

    draw_grid()
    draw_map()
    #draw_character(player_pos, PLAYER_COLOR)
    #draw_character(enemy_pos, ENEMY_COLOR)

    # Update the display
    pygame.display.flip()

pygame.quit()

