def points(ticket):
    ticket = ticket.split('|')
    winning_numbers = ticket[0].split()
    my_numbers = ticket[1].split()

    # n: number of winning numbers
    n = 0
    for number in my_numbers:
        if number in winning_numbers:
            n += 1

    if n == 1: return 1
    if n > 1: return 2**(n-1)
    else: return 0

if __name__ == '__main__':
    with open('data/day4.txt', 'r') as file:
        f = file.readlines()
        ans = []

        for ticket in f:
            ticket = (ticket.split(':'))[1]
            ans.append(points(ticket))
