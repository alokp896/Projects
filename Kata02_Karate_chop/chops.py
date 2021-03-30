def chop(ele, lst):
    return binary_search(ele, lst, indexes=0)


def binary_search(ele, lst, indexes = 0):
    if lst:
        lst = sorted(lst)
        mid = int(len(lst) / 2)
        mid_elem = lst[mid]
        if mid_elem == ele:
            return indexes + mid
        if mid_elem > ele:
            return binary_search(ele, lst[:mid], indexes)
        return binary_search(ele, lst[mid + 1:], indexes + mid + 1)
    else:
        return -1


# if __name__ == '__main__':
    # x = chop(6, [2, 12, 1, 3, 4, 15, 14, 7, 8, 10, 11, 12, 13])
    # print(x)