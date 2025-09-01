class SimpleDynamicArray:
    def __init__(self, initial_capacity=2):
        self.capacity = initial_capacity
        self.length = 0
        self.data = [None] * self.capacity
        print(f"Created dynamic array with initial capacity {self.capacity}")

    def __str__(self):
        return str([self.data[i] for i in range(self.length)])
    
    def _resize(self):
        old_capacity = self.capacity
        self.capacity *= 2
        