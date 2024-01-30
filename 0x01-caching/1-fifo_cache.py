#!/usr/bin/env python3
""" FIFOCache module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if None in (key, item):
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            for k, _ in self.cache_data.copy().items():
                print(f"DISCARD: {k}")
                del self.cache_data[k]
                break

    def get(self, key):
        """ Get an item by key
        """
        result = None
        if key in self.cache_data.keys() and key is not None:
            result = self.cache_data[key]
        return result
