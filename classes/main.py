from AI_engine import *
from text_UI import *
env = MazeEnv(size=5)
agent = Agent(env)

num_episodes = 500
for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0
    
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.store_transition(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward
        
        # Train the agent
        agent.train()
    
    if (episode + 1) % 50 == 0:
        print(f"Episode {episode + 1}: Total Reward = {total_reward:.2f}, Epsilon = {agent.epsilon:.3f}")

print("Training completed!")

state = env.reset()
done = False
env.render()

while not done:
    action = agent.choose_action(state)
    state, _, done = env.step(action)
    env.render()
