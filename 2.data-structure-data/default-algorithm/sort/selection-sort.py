arr = [7,2,6,5,9]

def selection_sort(arr):
    n =len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


sorted_arr = selection_sort(arr)

print(sorted_arr)