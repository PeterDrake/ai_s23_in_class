import random
import statistics
import math

def individual():
    result = ''
    for i in range(200):
        num = random.randint(0, 1)
        result += str(num)
    return result

target = individual()


def fitness(ind):
    return math.exp(sum([a == b for a, b in zip(ind, target)]))


def population():
    return [individual() for _ in range(1000)]


def max_fitness(p):
    return max(fitness(i) for i in p)


def min_fitness(p):
    return min(fitness(i) for i in p)


def mean_fitness(p):
    return statistics.mean(fitness(i) for i in p)


def select(p, fitnesses):
    spin = random.random() * sum(fitnesses)
    for i in range(len(p)):
        if spin < fitnesses[i]:
            return p[i]
        else:
            spin -= fitnesses[i]

def flip(bit):
    if bit == '0':
        return '1'
    else:
        return '0'

def mutate(ind):
    return ''.join([flip(b) if random.random() < 1/len(ind) else b for b in ind])

def cross(a, b):
    i = random.randint(0, len(a))
    return a[:i] + b[i:]

def evolve(p):
    fitnesses = [fitness(i) for i in p]
    return [mutate(cross(select(p, fitnesses), select(p, fitnesses))) for _ in range(len(p))]

p = population()
for i in range(100):
    p = evolve(p)
    print(math.log(mean_fitness(p)))
    print(math.log(max_fitness(p)))
    print()


