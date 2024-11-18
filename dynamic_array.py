class DynamicArray:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity
        print(self.array)

    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert_at_beginning(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        for i in range(self.size, 0, -1):
            self.array[i] = self.array[i - 1]
        self.array[0] = value
        self.size += 1

    def insert_at_end(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.size] = value
        self.size += 1

    def delete_from_beginning(self):
        if self.size == 0:
            raise IndexError("Boş bir diziden eleman silinemez.")
        for i in range(1, self.size):
            self.array[i - 1] = self.array[i]
        self.array[self.size - 1] = None
        self.size -= 1

    def delete_from_end(self):
        if self.size == 0:
            raise IndexError("Boş bir diziden eleman silinemez.")
        self.array[self.size - 1] = None
        self.size -= 1

    def __str__(self):
        return str(self.array[: self.size])


da = DynamicArray()
da.insert_at_end(10)
print("guncellenmiş liste : ", da)
da.insert_at_end(20)
print("guncellenmiş liste : ", da)
da.insert_at_beginning(5)
print("guncellenmiş liste : ", da)
da.insert_at_beginning(1)
print("guncellenmiş liste : ", da)
da.delete_from_beginning()
print("guncellenmiş liste : ", da)
da.delete_from_end()
print("guncellenmiş liste : ", da)

print(da)
