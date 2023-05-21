class SecondChanceCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.pointer = 0

    def get(self, key):
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache[i][1] = 1  # Set reference bit to 1
                return self.cache[i][2]
        return -1

    def put(self, key, value):
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache[i][2] = value  # Update value
                self.cache[i][1] = 1  # Set reference bit to 1
                return
        if len(self.cache) >= self.capacity:
            self.evict()  # Remove a key-value pair based on second-chance replacement strategy
        self.cache.append([key, 1, value])  # Add new key-value pair with reference bit set to 1

    def evict(self):
        while True:
            current = self.cache[self.pointer]
            if current[1] == 1:
                current[1] = 0  # Set reference bit to 0
                self.pointer = (self.pointer + 1) % len(self.cache)  # Move pointer to next position
            else:
                del self.cache[self.pointer]  # Remove the key-value pair
                self.pointer = self.pointer % len(self.cache)  # Update pointer position
                break

# Example usage:
cache = SecondChanceCache(3)
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')
print(cache.get(1))  # Output: A
print(cache.get(2))  # Output: B
cache.put(4, 'D')
print(cache.get(3))  # Output: -1 (not found)
print(cache.get(4))  # Output: D
