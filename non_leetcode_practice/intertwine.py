# [1, 4, 5,               6 , 9, 7, 2]  index = 1
# [1, 6, 4, 9, 6, 7, 2]
# [a1, b1, a2, b2, a3, b4 ......]

def intertwine(arr: list, index: int) -> list:
    '''
    i = left pointer
    j = right pointer

    define a loop, and its stopping conditions
        - append value(s) to ret
        - increment pointers
    '''
    ret = []

    i = 0
    j = index

    while (i < index) or (j < len(arr)):
        if i < index:
            ret.append(arr[i])
        if j < len(arr):
            ret.append(arr[j])

        i += 1
        j += 1

    print(ret)
    return ret

intertwine([1,4,5,6,9,7,2], 5)
