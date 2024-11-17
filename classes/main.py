from AI_engine import *
from mazeEnv import *
from enemy import Enemy
from random import randint



def trainAgentWithEnemy(env, agent, enemy, num_episodes=500):
    for episode in range(num_episodes):
        state = env.reset()
        done = False
        count = 0

        enemy.buildFirstGrid(env.map_memory)
        enemy.setVisibleArea(env.map_memory)

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.store_transition(state, action, reward, next_state, done)
            agent.train()
            state = next_state
            count += 1

            enemy.moveCharacter(env.map_memory, [randint(-1,1), randint(-1,1)])
            enemy.setVisibleArea(env.map_memory)
            enemy.updateOwnGrid()

            if count > 1000:
                break

        print(f"Episode {episode + 1} - Moves: {count}")

        agent.update_epsilon()

        if (episode + 1) % 50 == 0:
            print(f"Episode {episode + 1}: Epsilon = {agent.epsilon:.3f}")
            #agent.save_model()

    agent.save_model()
    print("Training complete. Final model saved.")
    
    return agent, env

obstacles = []
for i in range(5):
    coor = [randint(0, 4), randint(0, 4)]
    if coor != [0, 0] and coor != [4, 4]:
        obstacles.append(coor)

env = MazeEnv(5, obstacles)
agent = Agent(env)
enemy = Enemy("enemy", "sprite", [], 0, 0)

trainAgentWithEnemy(env, agent, enemy, )
# env.change_goal([2, 3])
# agent, env = trainAgent(env, agent, num_episodes=100)

env.render(show_path=True)

