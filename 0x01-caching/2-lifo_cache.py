#!/usr/bin/env python3
""" LIFOCache module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()
        last_key_in = None
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if None in (key, item):
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            last_key = self.last_key_in
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.last_key_in = key

    def get(self, key):
        """ Get an item by key
        """
        result = None
        if key in self.cache_data.keys() and key is not None:
            result = self.cache_data[key]
        return result
