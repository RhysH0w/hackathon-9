import torch
import torch.nn as nn
import torch.optim as optim
import random

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

class Agent:
    def __init__(self, env, lr=0.001, gamma=0.99, epsilon=1.0, epsilon_decay=0.995):
        self.env = env
        self.model = DQN(input_dim=2, output_dim=4)  # Input: agent position (x, y); Output: Q-values for 4 actions
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        self.criterion = nn.MSELoss()
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.memory = []
        self.batch_size = 32
    
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
        
        # Sample a batch of experiences
        batch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        
        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions)
        rewards = torch.FloatTensor(rewards)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones)
        
        # Calculate Q-values
        q_values = self.model(states).gather(1, actions.unsqueeze(-1)).squeeze(-1)
        with torch.no_grad():
            next_q_values = self.model(next_states).max(1)[0]
        
        # Calculate target
        targets = rewards + self.gamma * next_q_values * (1 - dones)
        
        # Update model
        loss = self.criterion(q_values, targets)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        # Decay epsilon
        self.epsilon *= self.epsilon_decay
