#!/usr/bin/python3
""" BaseCaching module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Create a class LRUCache """
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Must assign to the dictionary for the key key."""
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS and key not in\
                    self.keys:
                del_key = self.keys.pop()
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            if key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Must return the value"""
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key)
