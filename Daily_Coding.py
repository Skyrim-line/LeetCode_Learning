point = (0, 0)

steps = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
from collections import Counter

moves = "LR"
def f2():
    numbers = Counter(moves)
    print(numbers)
    return numbers['L'] == numbers['R'] and numbers['U'] == numbers['D']
f2()
