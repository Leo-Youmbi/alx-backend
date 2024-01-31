#!/usr/bin/env python3
""" LRUCache module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Represents an object that allows storing and
    retrieving items from a dictionary with a LRU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.least_keys_used = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if None in (key, item):
            return

        if len(self.cache_data) >= self.MAX_ITEMS and \
                key not in self.least_keys_used:

            # Discard the least recently used item (LRU)
            lru_key = self.least_keys_used.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")
        else:

            if key in self.least_keys_used:
                self.least_keys_used.remove(key)

        self.cache_data[key] = item
        self.least_keys_used.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys() and key is not None:
            # Update least_keys_used to mark the key as recently used
            self.least_keys_used.remove(key)
            self.least_keys_used.append(key)
            return self.cache_data[key]

        return None
