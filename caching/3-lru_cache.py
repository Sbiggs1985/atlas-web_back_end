#!/usr/bin/env python3

""" Importing collections and the base_caching """
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Initialize the cache as an ordered dictionary."""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache with LRU eviction if necessary."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

    def get(self, key):
        """Get an item from the cache by key."""
        if key is None:
            return None

        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
