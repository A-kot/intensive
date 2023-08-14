arr = [1, 2, 4, 6, 8, 11, 23, 37]
target = 11

left = 0
right = len(arr) - 1
while left < right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(mid)  # выводим индекс элемента в массиве
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid