import pygame

class RunMap:

    @staticmethod
    def runMap(player, playerSpawnPos, enemy, enemySpawnPos, grid):
        # Initialize Pygame
        pygame.init()

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
        DOOR_COLOR = (0, 0, 255)

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

        # Main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((255, 255, 255))  # Fill the screen with white
            draw_grid()
            draw_map()
            pygame.display.flip()

        pygame.quit()