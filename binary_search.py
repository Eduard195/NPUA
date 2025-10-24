
arr = [ 2,3, 5, 6 , 8, 7, 9, 5]
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "NO such number"

print(binary_search(arr, 9))