def merge(lst1, lst2):
    if not lst1 and lst2:
        return lst2[:]
    elif lst1 and not lst2:
        return lst1[:]
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])
print(merge([5, 7], [2, 4, 6]))
# print(merge([1, 3, 5], [2, 4, 6]))