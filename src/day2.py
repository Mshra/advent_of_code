from sys import exit

def power(game: str):
    hmap = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    game = game.split(':')
    del game[0]
    game = str(game[0])
    game = game.split(';')

    # set = ' 1 green, 1 blue, 1 red'
    for set in game:
        set = set.split(',')
        for ball in set:
            ball = ball.split()
            hmap[ball[1]] = max(int(ball[0]), hmap[ball[1]])

    return hmap

def get_cubes(dict):
    return dict['red']*dict['green']*dict['blue'

with open('data/day2.txt') as file:
    file = file.readlines()
    ans = 0

    for id in range(len(file)):
        ans += get_cubes(power(file[id]))
    
    print(ans)