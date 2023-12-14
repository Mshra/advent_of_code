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