# f('1 + 2 = 3')
# f('1_3 + 2_4 = 387')
# f('__ + ___ = ____')
# f('1_3 + 2_4 = 388')
# f('0_ + 00 = 0_ ')

# 有可能有多个solution
def f(expression):
    '''
    >>> f('1 + 2 = 3')
    >>> f('1_3 + 2_4 = 387')
    143 + 244 = 387
    >>> f('__ + ___ = ____')
    0 + 0 = 0
    >>> f('1_3 + 2_4 = 388')
    No solution!
    >>> f('0_ + 00 = 0_ ')
    0 + 0 = 0
    1 + 0 = 1
    2 + 0 = 2
    3 + 0 = 3
    4 + 0 = 4
    5 + 0 = 5
    6 + 0 = 6
    7 + 0 = 7
    8 + 0 = 8
    9 + 0 = 9
    '''
    parts = expression.split('=')
    left = parts[0].strip().split('+')
    target = parts[1].strip()
    num1, num2 = left[0].strip(), left[1].strip()
    # print(num1,num2)
    if '_' not in (num1 or num2 or target):
        return
    solution_found = False
    for i in range(10):
        current_num1 = num1.replace('_', str(i))
        current_num2 = num2.replace('_', str(i))
        current_target = target.replace('_', str(i))
        # print(current_num1, current_num2,current_target)
        if (int(current_num1) + int(current_num2)) == int(current_target):
            print(f'{int(current_num1)} + {int(current_num2)} = {int(current_target)}')
            solution_found = True
    if not solution_found:
        print('No solution!')


if __name__ == '__main__':
    import doctest

    doctest.testmod()