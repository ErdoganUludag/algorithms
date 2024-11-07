import random


array = [random.randint(0, 100) for _ in range(100)]


def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


target = int(input("Hangi elemanı arıyorsun: "))
index = linear_search(array, target)
if index != -1:
    print("Elemanı bulduk yeri:", index + 1)
    print(array[: index + 5])
else:
    print("Böyle bir eleman listede yok")
