def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

user_input = input("Enter numbers separated by spaces: ")
values = [int(x) for x in user_input.split()]

sorted_values = quick_sort(values)
print("Sorted array:", sorted_values)
