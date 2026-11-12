size = 11
table = [None] * size
keys = [22, 41, 53, 46, 30, 13, 1, 67]

for key in keys:
    index = key % size

    while table[index] is not None:
        index = (index + 1) % size

    table[index] = key

for i in range(size):
    print(i, ":", table[i])