arr = [7, 1, 3, 2, 8]

for i in range(1, len(arr)):
    curr = arr[i]
    j = i - 1
    while j >= 0 and curr < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = curr

print(arr)

