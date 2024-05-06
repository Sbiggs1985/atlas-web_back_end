#!/usr/bin/env python3

""" Importing collections and base_caching """
from collections import deque
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Initialize the cache with a deque to track order."""
    def __init__(self):
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

    def get(self, key):
        """Retrieve an item from the cache by key."""
        if key is None:
            return None

        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
