def countSort(input_array):
    M = max(input_array)
    count_array = [0] * (M + 1)
    for num in input_array:
        count_array[num] = count_array[num] + 1

    sorted_array = []
    for i, freq in enumerate(count_array):
        sorted_array.extend([i] * freq)

    return sorted_array


array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(countSort(array))
