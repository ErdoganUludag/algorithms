# radix sort bir tabab sıralaması fonksiyonudur.


def counting_sort(array, exp):
    n = len(array)
    output = [0] * n  # Sonuç dizisi
    count = [0] * 10  # Sayım dizisi (0-9 arası rakamlar için)

    # Belirli basamaktaki rakamların sayısını say
    for i in range(n):
        index = (array[i] // exp) % 10
        count[index] += 1

    # Sayım dizisini kümülatif hale getir
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Sonuç dizisini oluştur
    i = n - 1
    while i >= 0:
        index = (array[i] // exp) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1

    # Orijinal diziye sıralanmış değerleri yaz
    for i in range(n):
        array[i] = output[i]


def radix_sort(arr):
    # Dizideki maksimum değeri bul
    max_val = max(arr)

    # Her basamak için counting sort uygula
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Test etme
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sıralanmış dizi:", arr)
