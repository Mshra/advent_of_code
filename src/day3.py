if __name__ == '__main__':
    with open('data/day3.txt') as file:
        f = file.readlines()

        for engine_schematic in f:
            engine_schematic = engine_schematic[:len(engine_schematic) - 1]