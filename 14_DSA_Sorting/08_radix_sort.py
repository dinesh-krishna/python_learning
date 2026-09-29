def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    counts = [0] * 10

    for value in arr:
        digit = (value // exp) % 10
        counts[digit] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        counts[digit] -= 1
        output[counts[digit]] = arr[i]

    return output

def radix_sort(arr):
    if not arr:
        return arr

    maximum = max(arr)
    exp = 1
    while maximum // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr

user_input = input("Enter non-negative numbers separated by spaces: ")
values = [int(x) for x in user_input.split()]

sorted_values = radix_sort(values)
print("Sorted array:", sorted_values)
