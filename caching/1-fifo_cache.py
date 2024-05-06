#!/usr/bin/env python3

from base_caching import BaseCaching
from collections import deque
""" Importing the base_caching and collections """


class FIFOCache(BaseCaching):
    def __init__(self):
        """Initialize the cache with a deque to track order of insertion."""
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """Add an item to the cache with FIFO eviction if necessary."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.popleft()
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item from the cache by key."""
        if key is None:
            return None
        return self.cache_data.get(key, None)
