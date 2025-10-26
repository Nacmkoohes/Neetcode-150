class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Dictionary to hold the key-value pairs
        self.cache = {}
        # List to maintain the order of keys for LRU
        self.order = []


    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end of the order list
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the key to the end of the order list
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used item
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
            # Add the new key-value pair
            self.cache[key] = value
            self.order.append(key)