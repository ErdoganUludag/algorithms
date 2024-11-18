# time complexity is O(n+k)


def count_sort(input_array):
    M = max(input_array)

    count_array = [0] * (M + 1)

    for num in input_array:
        count_array[num] = count_array[num] + 1

    sorted_array = []
    for i, freq in enumerate(count_array):
        sorted_array.extend([i] * freq)

    return sorted_array


input_array = [9, 5, 7, 6, 4, 1, 2, 35, 10, 99, 45, 65, 35, 78, 34]
ordered_list = count_sort(input_array)
print(ordered_list)
