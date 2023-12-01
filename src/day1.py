def calibration_value(word):
    hmap = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num = []

    for i in range(len(word)):
        if word[i].isdigit():
            num.append(word[i])
        if word[i:i+3] in hmap:
            num.append(hmap[word[i:i+3]])
        if word[i:i+4] in hmap:
            num.append(hmap[word[i:i+4]])
        if word[i:i+5] in hmap:
            num.append(hmap[word[i:i+5]])

    return int(str(num[0]) + str(num[len(num)-1]))

with open('data/day1.txt', 'r') as file:
    arr = file.readlines()
    ans = 0
    values = []

    for word in arr:
        values.append(calibration_value(word[:len(word) - 1]))

    print(sum(values))