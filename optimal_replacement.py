class OptimalCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]  # Remove existing key-value pair
        elif len(self.cache) >= self.capacity:
            self.evict()  # Remove a key-value pair based on optimal replacement strategy
        self.cache[key] = value  # Add new key-value pair

    def evict(self):
        # Find a key to evict based on optimal replacement strategy
        future_indices = {key: len(self.cache) for key in self.cache}  # Initialize with maximum future index
        for i, key in enumerate(self.cache):
            if key in future_indices:
                future_indices[key] = min(future_indices[key], i)  # Update future index
        evict_key = min(future_indices, key=future_indices.get)  # Key with the minimum future index
        del self.cache[evict_key]  # Remove the key-value pair

# Example usage:
cache = OptimalCache(3)
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')
print(cache.get(1))  # Output: A
print(cache.get(2))  # Output: B
cache.put(4, 'D')
print(cache.get(3))  # Output: -1 (not found)
print(cache.get(4))  # Output: D
