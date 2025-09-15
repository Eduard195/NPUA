lst = [5, 6, 8, 4, 3, 1, 59, 14]
for i in range(len(lst)-1):
    min_ind = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_ind]:
            min_ind = j
    if min_ind != i:
        lst[i], lst[min_ind] =  lst[min_ind], lst[i]

print(lst)