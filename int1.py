arr = [9, 5, 8, 1, 2]

for _ in range(len(arr)):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            tp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tp

print(arr)