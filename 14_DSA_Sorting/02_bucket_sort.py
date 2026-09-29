def bucket_sort(arr):
    if not arr:
        return arr

    minimum, maximum = min(arr), max(arr)
    bucket_count = len(arr)
    bucket_range = (maximum - minimum) / bucket_count or 1
    buckets = [[] for _ in range(bucket_count)]

    for value in arr:
        index = min(int((value - minimum) / bucket_range), bucket_count - 1)
        buckets[index].append(value)

    sorted_values = []
    for bucket in buckets:
        sorted_values.extend(sorted(bucket))

    return sorted_values

user_input = input("Enter numbers separated by spaces: ")
values = [float(x) for x in user_input.split()]

sorted_values = bucket_sort(values)
print("Sorted array:", sorted_values)
