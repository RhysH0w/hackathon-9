from AI_engine import *
from text_UI import *

def test_agent(env, agent):
    state = env.reset()
    done = False
    total_reward = 0
    
    while not done:
        action = agent.choose_action(state)
        state, reward, done = env.step(action)
        total_reward += reward
    
    print(f"Test run: Total Reward = {total_reward:.2f}")
    env.render(show_path=True)

# Train the agent first, then run this test
env = MazeEnv(size=5)
agent = Agent(env)

# Training Loop (similar to the previous implementation)
num_episodes = 50
for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0
    count = 0
    
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.store_transition(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward
        
        # Train the agent
        agent.train()
        count += 1
        if count > 500:
            break
    print(f"Moves: {count}")
    
    if episode % agent.update_target_steps == 0:
        agent.update_target_network()
    
    if (episode + 1) % 50 == 0:
        print(f"Episode {episode + 1}: Total Reward = {total_reward:.2f}, Epsilon = {agent.epsilon:.3f}")

print("Training completed!")

# Test the agent and visualize the path
test_agent(env, agent)
