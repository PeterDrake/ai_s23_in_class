grid = [0, 0, 1, 0]


# def contains_1(g):
#     for n in g:
#         if n == 1:
#             return True
#     return False
#
#
# print(contains_1(grid))

# print(1 in grid)

def index_of(x, g):
    'Returns the index of x in g, or -1 if x is not present in g'
    i = 0
    while i < len(g):
        if g[i] == x:
            return i
        i += 1
    return -1

# print(index_of(1, grid))


import random

def generate_grid(n):
    result = []
    for i in range(n):
        result.append(random.randint(1, 100))
    return result

print(generate_grid(10))
