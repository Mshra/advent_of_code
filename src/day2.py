import sys

def valid(game: str):
    hmap = {
        'red': 12,
        'green': 13,
        'blue': 14
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
            if int(ball[0]) > hmap[ball[1]]:
                return False

    return True

with open('data/day2.txt') as file:
    file = file.readlines()
    ans = 0

    for id in range(len(file)):
        if valid(file[id]):
            ans += id + 1

    print(ans)