# tree = [2, [6, [7], [5], [1]], [3, [4]]]
#
# print(tree)

import random

def generate_tree(depth):
    result = [random.randint(1, 100)]
    if depth == 0:
        return result
    for i in range(random.randint(0, 3)):
        result.append(generate_tree(depth - 1))
    return result

tree = generate_tree(2)
print(tree)


def print_tree(tree, indent=''):
    print(indent + str(tree[0]))
    for child in tree[1:]:
        print_tree(child, indent + '  ')

print_tree(tree)


def largest(tree):
    '''
    Returns the largest element of tree, using depth-first search.
    '''
    result = tree[0]
    for child in tree[1:]:
        result = max(result, largest(child))
    return result

print(largest(tree))
