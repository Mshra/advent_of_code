def show_engine(schematic):
    for i in range(0, 100, 10):
        print(schematic[i:i+10])

def find_number(schematic):
    def parse_number(string):
        num = ''
        for c in string:
            if c.isdigit(): num += c
        return int(num)

    not_symbol = set([n for n in range(0, 10)] + ['.'])
    numbers = []

    for i in range(len(schematic)):
        if schematic[i] not in not_symbol:
            # check left adjacent
            if schematic[i - 1].isdigit():
                numbers.append(parse_number(schematic[i-3 : i]))

            # check right adjacent
            if schematic[i + 1].isdigit():
                numbers.append(parse_number(schematic[i+1 : i+4]))

            # check diagonally(previous)
            for j in range(i - 9, i - 12, -1):
                if schematic[j].isdigit():
                    pass
            # check diagonally(after)

            return sum(numbers)

if __name__ == '__main__':
    with open('data/day3.txt', 'r') as file:
        f = file.readlines()

        for schematic in f:
            show_engine(schematic)
            break