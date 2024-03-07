from itertools import zip_longest

def f(*x):
    '''
    >>> f(0, 0, 0)
    >>> f(1, 2, 3)
        *
      * *
    * * *
    >>> f(1, 2, 1, 0, 0, 0)
      *
    * * *
    >>> f(0, 2, 3, 4)
          *
        * *
      * * *
      * * *
    >>> f(4)
    *
    *
    *
    *
    >>> f(4, 4, 4)
    * * *
    * * *
    * * *
    * * *
    >>> f(4, 0, 2, 2)
    *
    *
    *   * *
    *   * *
    '''
    if any(x):
        lines = []
        for num in x:
            if num == 0:
                lines.append(' ')
            else:
                lines.append('*' * num)
        result=[]
        for i in zip_longest(*lines,fillvalue=' '):
            result.append(' '.join(i).rstrip())






if __name__ == '__main__':
    import doctest

    doctest.testmod()
