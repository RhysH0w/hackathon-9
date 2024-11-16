from AI_engine import *
from mazeEnv import *
from random import randint

def trainAgent(env, agent, num_episodes):
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

        print(f"Move count: {count}")

        agent.update_epsilon()

        if (episode + 1) % 50 == 0:
            print(f"Episode {episode + 1}: Epsilon = {agent.epsilon:.3f}")


    return agent, env

obstacles = []
for i in range(5):
    coor = [randint(0, 4), randint(0, 4)]
    if coor != [0, 0] and coor != [4, 4]:
        obstacles.append(coor)

env = MazeEnv(5, obstacles)
agent = Agent(env)
agent, env = trainAgent(env, agent, num_episodes=200)
# env.change_goal([2, 3])
# agent, env = trainAgent(env, agent, num_episodes=100)

env.render(show_path=True)


