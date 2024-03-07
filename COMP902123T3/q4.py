# 蛇形打印，从一个别的字母开始，
# 蛇形打印是从A开始，别的是从 O 开始
def f(height, width, starting_with = 'A'):
    '''
    >>> f(0, 0)
    >>> f(4, 0)
    A
    B
    C
    D
    >>> f(0, 4)
    ABCD
    >>> f(4, 4, 'X')
    XEFM
    YDGL
    ZCHK
    ABIJ

    >>> f(4,5,'X')
    XEFMN
    YDGLO
    ZCHKP
    ABIJQ
    '''
    alpha = ''
    if width == 0:
        for i in range(height):
            print(chr(ord('A') + i))
    elif height == 0:
        temp = ''
        for i in range(width):
            temp += chr(ord('A') + i)
        print(temp)

    d = ord(starting_with)
    result = []
    for i in range(width):
        alpha = ''
        for j in range(height):
            alpha += chr(d)
            d = (d - ord('A') + 1) % 26 + ord('A')  # 循环递增字母
        if i % 2 != 0: # 奇数行进行反向打印
            result.append(alpha[::-1])
        else:
            result.append(alpha)

    # print(result)
    for i in zip(*result):
        i="".join(i)
        if i:
            print(''.join(i))



if __name__ == '__main__':
    import doctest

    doctest.testmod()