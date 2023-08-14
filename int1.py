arr = [9, 5, 8, 1, 2]

for j in range(len(arr)):
    for i in range(len(arr)-1-j):
        if arr[i] > arr[i+1]:
            tp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tp

print(arr)
