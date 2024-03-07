# Given a dictionary D and a key x, there is a (unique) loop
# containing x if there are keys x_1, ..., x_k such that:
# D maps x to x_1
# D maps x_1 to x_2
# ...
# D maps x_{k-1} to x_k
# x_1, ..., x_{k-1} are all different to x and x_k is x
# (in the particular case where k = 1, D maps x to x).
#
# When the loop does not exist, the function prints out nothing.
# When the loop exists, the function prints out the loop,
# STARTING AND ENDING with the SMALLEST element in the loop.
#
# You can assume that the function is called with as first argument,
# a dictionary having nothing but integers as keys and values,
# and with as second argument, an integer.


def loop(D, x):
    '''
    >>> loop({1: 1}, 0)
    >>> loop({1: 2, 2: 2}, 1)
    >>> loop({1: 2, 2: 3}, 1)
    >>> loop({1: 2, 2: 3, 3: 2}, 1)
    >>> loop({1: 1}, 1)
    1--1
    >>> loop({1: 2, 2: 1}, 2)
    1--2--1
    >>> loop({12: 14, 13: 14, 14: 7, 7: 12, 6: 8, 8: 6, 5: 11}, 14)
    7--12--14--7
    >>> loop({0: 4, 1: 0, 2: 1, 3: 2, 4: 7, 5: 6, 6: 4, 7: 0, 8: 8, 9: 4}, 4)
    0--4--7--0
    >>> loop({0: 7, 1: 7, 2: 3, 3: 8, 4: 6, 5: 8, 6: 6, 7: 4, 8: 9, 9: 2}, 8)
    2--3--8--9--2
    '''
    # dictionary
    result = []
    current_key = x
    if current_key not in D.keys():  # 如果当前key不在字典的key中则返回说明没找到
        return
    while D[current_key] != x:  # 如果字典的key对应的值不是x就可以继续循环x=2,2:2则不满足条件
        if D[current_key] in result:
            return
        if D[current_key] not in D.keys():  # 如果当前key对应的value不在字典的key中则返回说明没找到
            return
        result.append(current_key)  # 把当前key对应的value加入到result中
        current_key = D[current_key]  # 每次循环更新当前的key，继续找下一次的value看是否和key一样

    result.append(current_key)  # 如果key=x的话把x加入到result中
    min_number = min(result)
    min_index = result.index(min_number)  # 将result 列表中最小值对应的索引找出来
    result = result[min_index:] + result[:min_index]  # 将最小索引后面对应的数字和前面对应的数字加起来
    result.append(result[0])  # 将第一个元素放到最后
    print("--".join(str(i) for i in result))
    print("skyrim")
    for i in range(10):
        print(i)
        if i == 5:
            break


loop({0: 7, 1: 7, 2: 3, 3: 8, 4: 6, 5: 8, 6: 6, 7: 4, 8: 9, 9: 2}, 8)
