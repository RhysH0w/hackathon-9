from classes.character import Character
from static.static import *
from mazeEnv import MazeEnv

import torch
import torch.nn as nn
import torch.optim as optim
import random
import os

class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, output_dim)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

class Enemy(Character):
    def __init__(self, sprite, inventory, posx, posy, env=MazeEnv(5)):
        #super().__init__(self, name, sprite, inventory, posx, posy)
        #The super() call automatically passes self to the Character class, so you don’t need to include self explicitly. 
        super().__init__('Enemy', sprite, inventory, posx, posy)
        self._ownGrid = []

        self.model_path = "dqn_model.pth"
        self.model = DQN(input_dim=4, output_dim=4)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.epsilon = 1.0
        self.load_model()

        self.env = env
        self.criterion = nn.MSELoss()
        self.gamma = 0.95
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.memory = []
        self.batch_size = 32
        
    def buildFirstGrid(self, grid):
        ownGrid = []
        for i in range (len(grid)):
            ownGrid.append([])
            for j in range (len(grid[0])):
                ownGrid[i].append(-1)

    def updateOwnGrid(self):
        ownGrid = self._ownGrid
        visibleArea = self._visibleArea
        for x, y, value in visibleArea:
            ownGrid[x][y] = value
        self._ownGrid = ownGrid


    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 3)  # Explore
        else:
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            q_values = self.model(state_tensor)
            return torch.argmax(q_values).item()  # Exploit
    
    def store_transition(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
        if len(self.memory) > 1000:
            self.memory.pop(0)
    
    def train(self):
        if len(self.memory) < self.batch_size:
            return
        
        batch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        
        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions)
        rewards = torch.FloatTensor(rewards)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones)
        
        q_values = self.model(states).gather(1, actions.unsqueeze(-1)).squeeze(-1)
        with torch.no_grad():
            next_q_values = self.model(next_states).max(1)[0]
        targets = rewards + self.gamma * next_q_values * (1 - dones)
        
        loss = self.criterion(q_values, targets)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        #Decay epsilon
        self.epsilon *= self.epsilon_decay

    def update_epsilon(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
    
    def save_model(self):
        checkpoint = {
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'epsilon': self.epsilon,
        }

        torch.save(checkpoint, self.model_path)
        print(f"Model saved to {self.model_path}")

    def load_model(self):
        if os.path.exists(self.model_path):
            checkpoint = torch.load(self.model_path)
            self.model.load_state_dict(checkpoint['model_state_dict'])
            self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
            self.epsilon = checkpoint.get('epsilon', 1.0)
            print(f"Model loaded from {self.model_path}")
        else:
            print("No saved model found. Starting fresh.")


    

