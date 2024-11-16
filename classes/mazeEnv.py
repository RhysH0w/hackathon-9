import numpy as np
import matplotlib.pyplot as plt

class MazeEnv:
    def __init__(self, size=5):
        self.size = size
        self.reset()
    
    def reset(self):
        self.agent_pos = [0, 0]  # Start at the top-left corner
        self.goal_pos = [self.size - 1, self.size - 1]  # Goal at the bottom-right corner
        self.path = [self.agent_pos.copy()]
        return self.get_state()
    
    def get_state(self):
        return [self.agent_pos[0], self.agent_pos[1], self.goal_pos[0], self.goal_pos[1]]
    
    def step(self, action):
        # Actions: 0=up, 1=down, 2=left, 3=right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        new_pos = [self.agent_pos[0] + moves[action][0], self.agent_pos[1] + moves[action][1]]
        
        # Check if the new position is within bounds
        if 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size:
            self.agent_pos = new_pos
        
        # Track the path
        self.path.append(self.agent_pos.copy())
        
        # Reward for reaching the goal
        if self.agent_pos == self.goal_pos:
            return self.get_state(), 1.0, True  # Reward for reaching the goal
        
        # Small penalty for each move to encourage efficiency
        return self.get_state(), -0.01, False
    
    def render(self, show_path=True):
        grid = np.zeros((self.size, self.size))
        grid[self.goal_pos[0], self.goal_pos[1]] = 2  # Goal
        grid[self.agent_pos[0], self.agent_pos[1]] = 1  # Agent's position
        
        plt.figure(figsize=(6, 6))
        plt.imshow(grid, cmap='coolwarm', origin='upper')

        if show_path:
            path = np.array(self.path)
            plt.plot(path[:, 1], path[:, 0], marker='o', color='white', linewidth=2, markersize=5)

        plt.xticks(range(self.size))
        plt.yticks(range(self.size))
        plt.grid(True)
        plt.show()
