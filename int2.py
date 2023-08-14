arr = [1, 2, 9, 5, 7, 8]

maximum = -1000000
ind_max = 0

for j in range(len(arr)):
    for i in range(len(arr)-j):
        if arr[i] > maximum:
            maximum = arr[i]
            ind_max = i
    tp = maximum
    arr[ind_max] = arr[len(arr)-1-j]
    arr[len(arr)-1-j] = tp
    maximum = -100000

print(arr)

