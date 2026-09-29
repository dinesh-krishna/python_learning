def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

user_input = input("Enter numbers separated by spaces: ")
values = [int(x) for x in user_input.split()]

sorted_values = selection_sort(values)
print("Sorted array:", sorted_values)
