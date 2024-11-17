import pygame

class RunMap:

    @staticmethod
    def runMap(player, playerSpawnPos, enemy, enemySpawnPos, grid):
        # Initialize Pygame
        pygame.init()


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

        # Set up grid dimensions
        GRID_ROWS = len(grid)
        GRID_COLS = len(grid[0])
        CELL_WIDTH = SCREEN_WIDTH // GRID_COLS
        CELL_HEIGHT = SCREEN_HEIGHT // GRID_ROWS

        # Set player and enemy positions
        player_pos = playerSpawnPos
        enemy_pos = enemySpawnPos

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

        def draw_map():
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    x = col * CELL_WIDTH
                    y = row * CELL_HEIGHT
                    if [row, col] == player_pos:
                        color = PLAYER_COLOR
                    elif [row, col] == enemy_pos:
                        color = ENEMY_COLOR
                    elif grid[row][col] == 1:  # WALL
                        color = WALL_COLOR
                    elif grid[row][col] == 2:  # DOOR
                        color = DOOR_COLOR
                    else:
                        color = (255, 255, 255)  # Default color for empty cells
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
        # Main game loop
        running = True
        while running:
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

            # Move the enemy
            move_enemy()  # Move the enemy after the player moves

            screen.fill((255, 255, 255))  # Fill the screen with white
            draw_grid()
            draw_map()
            pygame.display.flip()

        pygame.quit()