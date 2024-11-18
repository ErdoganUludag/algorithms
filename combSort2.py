def defineGap(gap):
    gap = gap * 10 // 13
    if gap < 1:
        return 1
    return gap


def combSort(array):
    gap = len(array)

    while gap != 1:
        gap = defineGap(gap)
        for i in range(0, len(array) - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]


array = [95, 54, 19, 789, 63, 12, 10, 2, 6, 4, 2, 545, 36, 74, 41, 68]
combSort(array)
print(array)
