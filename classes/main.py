from AI_engine import *
from mazeEnv import *

env = MazeEnv(size=5)
agent = Agent(env)
agent, env = trainAgent(env, agent, num_episodes=100)
# env.change_goal([2, 3])
# agent, env = trainAgent(env, agent, num_episodes=100)

env.render(show_path=True)


def trainAgent(env, agent, num_episodes=500):
    for episode in range(num_episodes):
        state = env.reset()
        done = False
        count = 0

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.store_transition(state, action, reward, next_state, done)
            agent.train()
            state = next_state
            count += 1
            if count > 100:
                break

        print(f"Episode {episode + 1} - Moves: {count}")

        agent.update_epsilon()

        if (episode + 1) % 50 == 0:
            print(f"Episode {episode + 1}: Epsilon = {agent.epsilon:.3f}")

    agent.save_model()
    print("Training complete. Final model saved.")
    
    return agent, env