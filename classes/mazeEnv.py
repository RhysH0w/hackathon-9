import numpy as np
import matplotlib.pyplot as plt
from random import randint

class MazeEnv:
    def __init__(self, size, obstacles=[[2, 2], [3, 3]]):
        self.size = size
        self.obstacles = obstacles
        self.visited = None  # To track visited squares
        self.sight = []
        self.reset()
    
    def reset(self):
        self.agent_pos = [0, 0]  # Start at the top-left corner
        self.goal_pos = [self.size - 1, self.size - 1]  # Goal at the bottom-right corner
        self.visited = np.zeros((self.size, self.size))  # Reset visited squares
        self.visited[0, 0] = 1  # Mark starting position as visited
        self.path = [self.agent_pos.copy()]
        self.obstacles = self.createRandomObstacles(self.size)
        return self.get_state()
    
    def get_state(self):
        adj_nodes = self.get_adjecent_nodes()
        return [self.agent_pos[0], self.agent_pos[1], self.goal_pos[0], self.goal_pos[1]] + adj_nodes + self.visited.flatten().tolist()
    
    def get_adjecent_nodes(self):
        moves = self.get_sight()
        adj_info = []

        for move in moves:
            new_pos = [self.agent_pos[0] + move[0], self.agent_pos[1]+move[1]]

            if (0 <= new_pos[0] < self.size and 0 < new_pos[1] < self.size):
                if new_pos == self.agent_pos:
                    adj_info.append(999) #Goal
                elif new_pos in self.obstacles:
                    adj_info.append(1) #Obstacle
                else:
                    adj_info.append(0) #Blank space
            else:
                adj_info.append(-1)
        return adj_info
    
    def step(self, action):
        # Actions: 0=up, 1=down, 2=left, 3=right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        new_pos = [self.agent_pos[0] + moves[action][0], self.agent_pos[1] + moves[action][1]]
        
        # Check if the new position is within bounds
        if (0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size) and new_pos not in self.obstacles:
            self.agent_pos = new_pos

        # Track the path
        self.path.append(self.agent_pos.copy())
        
        # Reward for reaching the goal
        if self.agent_pos == self.goal_pos:
            return self.get_state(), 10.0, True  # Reward for reaching the goal
        
         # Exploration bonus for unvisited squares
        exploration_bonus = 0
        if self.visited[self.agent_pos[0], self.agent_pos[1]] == 0:
            exploration_bonus = 0.1  # Reward for exploring a new square
            self.visited[self.agent_pos[0], self.agent_pos[1]] = 1
        # else:
        #     exploration_bonus = -0.1
            
        # Small penalty for each move to encourage efficiency
        return self.get_state(), -0.02 + exploration_bonus, False
        
    
    def render(self, show_path=True):
        grid = np.zeros((self.size, self.size))
        grid[self.goal_pos[0], self.goal_pos[1]] = 2  # Goal
        grid[self.agent_pos[0], self.agent_pos[1]] = 1  # Agent's position
        
        plt.figure(figsize=(6, 6))
        plt.imshow(grid, cmap='coolwarm', origin='upper')

        if show_path:
            path = np.array(self.path)
            plt.plot(path[:, 1], path[:, 0], marker='o', color='white', linewidth=2, markersize=5)

            for item in self.obstacles:
                plt.plot(item[1], item[0], marker='s', color='black', markersize=10)

        plt.xticks(range(self.size))
        plt.yticks(range(self.size))
        plt.grid(True)
        plt.show()

    def createRandomObstacles(self, size):
        obstacles = []
        for i in range(5):
            coor = [randint(0, size - 1), randint(0, size - 1)]
            if coor not in [[0, 0], [1, 0], [0, 1],  [size - 1, size - 1]]:
                obstacles.append(coor)
        return obstacles
    
    def add_sight(self, square):
        self.sight.append(square)

    def get_sight(self):
        return self.sight