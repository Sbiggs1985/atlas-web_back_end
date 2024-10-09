#!/usr/bin/env python3

""" Importing the base_caching and collections"""
from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """Initialize the cache with a deque to track the order of insertion."""
    def __init__(self):
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """Add an item to the cache with LIFO eviction if necessary."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache by key."""
        if key is None:
            return None  # If key is None, return None
        return self.cache_data.get(key, None)
