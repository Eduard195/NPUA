import math

arr = [5, 6, 8, 47,  65, 86, 95,  213, 516]
import math

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

   
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return "no such element"

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return "No such element"



print(jump_search(arr, 516))