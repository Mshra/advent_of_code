def find_location(location, desert_map):
    for index in range(len(desert_map)):
        if desert_map[index][:3] == location:
            return index

with open('data/day8.txt', 'r') as file:
    # ready the data
    def func(location):
        return location[:len(location) - 1]
    instruction = file.readline()[:281]
    file.readline() # to jump over blank line
    desert_map = list(map(func, file.readlines()))

    d_map = {
        'L': 0,
        'R': 1
    }
    steps = 0

    location = desert_map[find_location('AAA', desert_map)]

    for direction in instruction:
        print(location)
        if location[:3] == 'ZZZ':
            print(steps)

        if d_map[direction]: # take right
            location = desert_map[find_location(location[12:15], desert_map)]
        else: # take left
            location = desert_map[find_location(location[7:10], desert_map)]

        steps += 1