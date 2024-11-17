import pygame
from mazeEnv import MazeEnv
from enemy import Enemy
import numpy as np

class RunMap:

    @staticmethod
    def runMap(player, enemy, playerSpawnPos=[0,0], enemySpawnPos=[8, 8], grid=[]):
        # Initialize Pygame
        pygame.init()


        GROUND = 0
        WALL = 1
        DOOR = 2

        # Set up display
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Run Map")

        # Set up colors
        GRID_COLOR = (200, 200, 200)
        PLAYER_COLOR = (0, 255, 0)
        ENEMY_COLOR = (255, 0, 0)
        WALL_COLOR = (0, 0, 0)
        DOOR_COLOR = (165, 42, 42)
        INVENTORY_COLOR = (255, 255, 0)

        # Set up grid dimensions
        GRID_ROWS = len(grid)
        GRID_COLS = len(grid[0])
        CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
        CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS

        # Set player and enemy positions
        player_pos = list(playerSpawnPos)
        enemy_pos = list(enemySpawnPos)

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

        def createObjectMap():
            objectMap = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    if grid[row][col] == 1:
                        objectMap.append([row, col, WALL])

        def draw_map(enemy_pos, player_pos):
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    x = col * CELL_WIDTH
                    y = row * CELL_HEIGHT
                    if [row, col] == player_pos:
                        color = PLAYER_COLOR
                    elif [row, col] == enemy_pos:
                        color = ENEMY_COLOR
                    elif grid[row][col] == GROUND: # 0
                        color = (255, 255, 255)
                    elif grid[row][col] == WALL:  # 1
                        color = WALL_COLOR
                    elif grid[row][col] == DOOR:  # 2
                        color = DOOR_COLOR
                    else:
                        color = (255, 255, 255)  # Default color for empty cells
                    pygame.draw.rect(screen, color, (x, y, CELL_WIDTH, CELL_HEIGHT))

        def draw_inventory():
            """Draw the player's inventory as a toolbar at the top of the screen."""
            inventory = player._inventory[:3]  # Get the first 3 items
            for i, item in enumerate(inventory):
                x = i * CELL_WIDTH
                y = 0
                pygame.draw.rect(screen, INVENTORY_COLOR , (x, y, CELL_WIDTH, CELL_HEIGHT))
                # Optionally, you can add text or images to represent the items

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


        def check_collision(player_pos, enemy_pos):
            """Check if the player and enemy are on the same position."""
            return player_pos == enemy_pos

        def render_screen(screen, enemy_pos, player_pos):
            screen.fill((255, 255, 255))  # Fill the screen with white
            draw_inventory()  # Draw the player's inventory
            draw_grid()
            draw_map(enemy_pos, player_pos)
            pygame.display.flip()
            return screen
        
    
        for row in range(GRID_ROWS):
            for value in range(GRID_COLS):
                if grid[row][value] == 1:
                    x = value
                    y = row
                    enemy.env.obstacles.append([y, x])

        for i in enemy.env.obstacles:
            print(i)


        # Main game loop
        running = True

        # Implement enemy second turn
        secondTurn = 5

        while running:

            screen = render_screen(screen, enemy_pos, player_pos)

            player_moved = False
            while not player_moved:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        player_moved = True
                    elif event.type == pygame.KEYDOWN:  # Handle arrow key presses
                        move_player(event.key)
                        player_moved = True

            if not running:
                break

            screen = render_screen(screen ,enemy_pos, player_pos)

            player.update_position(player_pos)


            # Move the enemy
            enemy.posx = enemy_pos[0]
            enemy.posy = enemy_pos[1]

            enemy.updateGoal(player_pos)
            enemy.trainEnemy(1)

            env = enemy.getEnv()
            path = np.array(env.path)
            print("Path: ", path)
            print( "End goal: ", env.goal_pos)
            enemy_pos = env.path[1]
            print(f"Enemy position: {enemy_pos}")

            enemy.update_position(enemy_pos)
            secondTurn -= 1

            if secondTurn == 0:
                # Move the enemy again
                enemy.posx = enemy_pos[0]
                enemy.posy = enemy_pos[1]

                enemy.updateGoal(player_pos)
                enemy.trainEnemy(1)

                env = enemy.getEnv()
                path = np.array(env.path)
                print("Path: ", path)
                print( "End goal: ", env.goal_pos)
                enemy_pos = env.path[1]
                print(f"Enemy position: {enemy_pos}")

                secondTurn = 5

            # Check for collision
            if check_collision(player_pos, enemy_pos):
                print("Collision detected!")

            enemy.update_position(enemy_pos)
                
        pygame.quit()