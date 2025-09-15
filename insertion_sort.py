lst = [3, 5, 3, 58, 4, 5, 7]
for i in range(1, len(lst)):
    current = lst[i]
    j = i-1
    while current < lst[j]:
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = current
print(lst)