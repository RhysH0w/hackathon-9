from enemy import *
from mazeEnv import *
from random import randint

env = MazeEnv(5)
enemy = Enemy(env=env)
# enemy, env = trainEnemy(env, enemy, 200)
enemy.trainEnemy(100)

env.render(show_path=True)

