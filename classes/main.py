from run_map import RunMap
from player import Player
from enemy import Enemy
from mazeEnv import MazeEnv

def main(player, enemy, grid):
    
    RunMap.runMap(player=player, enemy=enemy, grid=grid)

if __name__ == "__main__":
    player = Player("player", "sprite", [], 0, 0)

    env = MazeEnv(10)
    enemy = Enemy(env=env, posx=8, posy=8, sightRange=1)

    #enemy = Enemy("enemy", "sprite", [], 9, 9)
    grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 2, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    main(player, enemy, grid)


def console_mode(player, enemy, grid):
    print("Console mode")
    print("Press 'q' to quit")
    while True:
        user_input = input("Enter a movement or show options: ")
        if user_input == "q":
            break
        elif user_input == "w":
            player.moveCharacter(grid, (-1, 0))
        elif user_input == "a":
            player.moveCharacter(grid, (0, -1))
        elif user_input == "s":
            player.moveCharacter(grid, (1, 0))
        elif user_input == "d":
            player.moveCharacter(grid, (0, 1))
        elif user_input == "o":
            count = 0
            for item in player.getInventory():
                count+=1
                print(f"{count}) {item.name}")
            option = input("Choose an option: ")


# from enemy import *
# from mazeEnv import *
# from random import randint

# env = MazeEnv(5)
# enemy = Enemy(env=env)
# # enemy, env = trainEnemy(env, enemy, 200)
# enemy.trainEnemy(100)

# env.render(show_path=True)

