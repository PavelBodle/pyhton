# Bubble Sort

arr = [5, 4, 8, 9, 25, 5, 5, 8, 14, 56, 28]


def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble(arr))
