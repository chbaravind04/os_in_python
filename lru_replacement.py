class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.cache.move_to_end(key)  # Move accessed key to the end to represent most recently used
            return value
        return -1

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]  # Remove existing key-value pair
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove the least recently used key-value pair
        self.cache[key] = value  # Add new key-value pair

# Example usage:
cache = LRUCache(3)
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')
print(cache.get(1))  # Output: A
print(cache.get(2))  # Output: B
cache.put(4, 'D')
print(cache.get(3))  # Output: -1 (not found)
print(cache.get(4))  # Output: D
