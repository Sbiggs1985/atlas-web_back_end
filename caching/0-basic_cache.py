#!/usr/bin/env python3

""" Creating a Basic Dictionary """
from base_caching import BaseCaching
""" Documenting my class and creating imports"""


class BasicCache(BaseCaching):
    """ Documenting the class """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ This is the function called put """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Using the get function"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
