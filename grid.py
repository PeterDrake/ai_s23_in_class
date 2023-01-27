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
#
#
# def largest(g):
#     greatest = g[0]
#     for n in g:
#         if n > greatest:
#             greatest = n
#     return greatest
#
# grid = generate_grid(10)
# print(grid)
# print(largest(grid))

def generate_grid_2d(m, n):
    result = []
    for i in range(m):
        result.append(generate_grid(n))
    return result

grid = generate_grid_2d(4, 5)
print(grid)

def largest_2d(g):
    greatest = g[0][0]
    for i in g:
        greatest = max(greatest, max(i))
    return greatest

print(largest_2d(grid))
