num = [5, 6, 18 , 56, 23, 1, 4]

for i in range(len(num)):
    for j in range(len(num) - i - 1):
        if num[j] > num [j+1]:
            num[j], num[j + 1] = num [j + 1], num[j]

print(num)