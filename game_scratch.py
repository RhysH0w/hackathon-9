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
inventory_enemy = []
inventory_player = []
enemy = Enemy("enemy", "demon.jpg", inventory_enemy, 9, 9)
player = Player("player", "player.jpg", inventory_player, 0, 0)

print("health:" + str(enemy._health))
print(player.getPosx())
print(player._posx)

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
            if [row, col] == [player._posy, player._posx]:
                color = PLAYER_COLOR
            elif [row, col] == [enemy._posy, enemy._posx]:
                color = ENEMY_COLOR
            elif grid[row][col] == WALL:
                color = WALL_COLOR
            elif grid[row][col] == DOOR:
                color = DOOR_COLOR
            else:
                continue  # Skip empty cells

            pygame.draw.rect(screen, color, (x, y, CELL_WIDTH, CELL_HEIGHT))

def move_player(key):
    """Move the player on the grid based on the arrow keys."""
    if key == pygame.K_UP and player._posy > 0 and grid[player._posy - 1][player._posx] != WALL:  # Move up
        player._posy -= 1
    elif key == pygame.K_DOWN and player._posy < GRID_ROWS - 1  and grid[player._posy + 1][player._posx] != WALL:  # Move down
        player._posy += 1
    elif key == pygame.K_LEFT and player._posx > 0 and grid[player._posy][player._posx - 1] != WALL:  # Move left
        player._posx -= 1
    elif key == pygame.K_RIGHT and player._posx < GRID_COLS - 1 and grid[player._posy][player._posx + 1] != WALL:  # Move right
        player._posx += 1

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

    # Update the display
    pygame.display.flip()

pygame.quit()

