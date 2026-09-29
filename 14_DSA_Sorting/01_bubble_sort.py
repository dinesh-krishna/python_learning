def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

user_input = input("Enter numbers separated by spaces: ")
values = [int(x) for x in user_input.split()]

sorted_values = bubble_sort(values)
print("Sorted array:", sorted_values)