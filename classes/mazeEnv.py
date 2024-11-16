import numpy as np
import matplotlib.pyplot as plt

class MazeEnv:
    def __init__(self, size, obstacles):
        self.size = size
        self.obstacles = obstacles
        self.visited = None  # To track visited squares
        self.agent_pos = [0,0]
        self.goal_pos = [self.size -1, self.size -1]
        self.agent_pos = [0,0]
        self.goal_pos = [self.size -1, self.size -1]
        self.reset()
    
    def reset(self):
        self.agent_pos = [0, 0]  # Start at the top-left corner
        self.goal_pos = [self.size - 1, self.size - 1]  # Goal at the bottom-right corner
        self.visited = np.zeros((self.size, self.size))  # Reset visited squares
        self.visited[0, 0] = 1  # Mark starting position as visited
        self.map_memory = np.zeros((self.size, self.size))
        self.update_map_memory(self.agent_pos,1)
        for obstacle in self.obstacles:
            self.update_map_memory(obstacle, -1)
        self.update_map_memory(self.goal_pos, 2)
        self.map_memory = np.zeros((self.size, self.size))
        self.update_map_memory(self.agent_pos,1)
        for obstacle in self.obstacles:
            self.update_map_memory(obstacle, -1)
        self.update_map_memory(self.goal_pos, 2)
        self.path = [self.agent_pos.copy()]
        return self.get_state()
    
    def update_map_memory(self, position, value):
        self.map_memory[position[0], position[1]] = value
    
    def update_map_memory(self, position, value):
        self.map_memory[position[0], position[1]] = value
    
    def get_state(self):
        return [self.agent_pos[0], self.agent_pos[1], self.goal_pos[0], self.goal_pos[1]]
    
    def step(self, action):
        # Actions: 0=up, 1=down, 2=left, 3=right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        new_pos = [self.agent_pos[0] + moves[action][0], self.agent_pos[1] + moves[action][1]]
        
        # Check if the new position is within bounds
        if (0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size) and new_pos not in self.obstacles:
            self.agent_pos = new_pos
            self.update_map_memory


        # Track the path
        self.path.append(self.agent_pos.copy())


        
        # Reward for reaching the goal
        if self.agent_pos == self.goal_pos:
            return self.get_state(), 100.0, True  # Reward for reaching the goal
        else:
            return self.get_state(), -0.01, False
        
         # Exploration bonus for unvisited squares
        exploration_bonus = 0
        if self.visited[self.agent_pos[0], self.agent_pos[1]] == 0:
            exploration_bonus = 0.1  # Reward for exploring a new square
            self.visited[self.agent_pos[0], self.agent_pos[1]] = 1
        else:
            exploration_bonus = -0.1
            else:
            return self.get_state(), -0.01, False
        
        # Small penalty for each move to encourage efficiency
        return self.get_state(), -0.01 + exploration_bonus, False
        
    
    def render(self, show_path=True):
        grid = np.zeros((self.size, self.size))
        grid[self.goal_pos[0], self.goal_pos[1]] = 2  # Goal
        grid[self.agent_pos[0], self.agent_pos[1]] = 1  # Agent's position

        for obstacle in self.obstacles:
            grid[obstacle[0], obstacle[1]] = -1

        for obstacle in self.obstacles:
            grid[obstacle[0], obstacle[1]] = -1
        
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
        plt.title("Maze Environment")
        plt.show()
