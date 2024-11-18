# comb sort has similar logic to bubble sort. However,
# instead of comparing individual data like bubble sort,
# it makes range comparisons. This makes the process faster. Its complexity is n**2


def defineGap(gap):
    gap = gap * 10 // 13
    if gap < 1:
        return 1
    return gap


def combSort(array):
    length = len(array)
    gap = length
    swapped = True

    while gap != 1 or swapped:
        gap = defineGap(gap)
        swapped = False

        for i in range(length - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True


array = [95, 54, 19, 789, 63, 12, 10, 2, 6, 4, 2, 545, 36, 74, 41, 68]
combSort(array)
print(array)
