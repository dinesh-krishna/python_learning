def counting_sort(arr):
    if not arr:
        return arr

    minimum, maximum = min(arr), max(arr)
    counts = [0] * (maximum - minimum + 1)

    for value in arr:
        counts[value - minimum] += 1

    sorted_values = []
    for offset, count in enumerate(counts):
        sorted_values.extend([offset + minimum] * count)

    return sorted_values

user_input = input("Enter numbers separated by spaces: ")
values = [int(x) for x in user_input.split()]

sorted_values = counting_sort(values)
print("Sorted array:", sorted_values)
