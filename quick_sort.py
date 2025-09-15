lst = [5, 6, 8, 4, 3, 1, 59, 14]

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    less = []
    equal = [pivot]
    great = []
    for i in lst[:-1]:
        if i > pivot:
            great.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            less.append(i)
    return quick_sort(less) + equal + quick_sort(great)


print(quick_sort(lst))