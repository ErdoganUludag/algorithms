# TimSort'un temel işleyişi
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    left_len = mid - left + 1
    right_len = right - mid
    left_arr = arr[left : mid + 1]
    right_arr = arr[mid + 1 : right + 1]

    i = j = 0
    k = left
    while i < left_len and j < right_len:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < left_len:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < right_len:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def timsort(arr):
    min_run = 32  # Minimal run size for insertion sort

    # Apply insertion sort to small chunks of the array
    for i in range(0, len(arr), min_run):
        insertion_sort(arr, i, min((i + min_run - 1), len(arr) - 1))

    # Merge sorted chunks
    size = min_run
    while size < len(arr):
        for start in range(0, len(arr), size * 2):
            mid = min(len(arr) - 1, start + size - 1)
            end = min((start + size * 2 - 1), (len(arr) - 1))
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2


# Örnek kullanım
arr = [5, 21, 7, 23, 19, 10, 2, 14, 3, 12]
print("Başlangıç dizisi:", arr)
timsort(arr)
print("Sıralanmış dizi:", arr)
