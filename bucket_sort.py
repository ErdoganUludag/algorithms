def bucket_sort(arr):
    # 1. Boş kova listesi oluştur
    if len(arr) == 0:
        return arr

    # 2. En küçük ve en büyük değeri bul
    min_value = min(arr)
    max_value = max(arr)

    # 3. Kovaların sayısını belirle (burada basitçe array uzunluğu kadar seçiyoruz)
    bucket_count = len(arr)

    # 4. Kovaları oluştur
    buckets = [[] for _ in range(bucket_count)]

    # 5. Elemanları uygun kovalara yerleştir
    for num in arr:
        index = int((num - min_value) / (max_value - min_value) * (bucket_count - 1))
        buckets[index].append(num)

    # 6. Her kovayı sırala (genellikle bir sıralama algoritması kullanılır, burada varsayılan olarak sorted kullanıyoruz)
    for i in range(bucket_count):
        buckets[i] = sorted(buckets[i])

    # 7. Sıralı kovaları birleştir
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


# Örnek kullanım
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
