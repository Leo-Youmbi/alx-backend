#!/usr/bin/env python3
""" BaseCaching module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if None in (key, item):
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        result = None
        if key in self.cache_data.keys() and key is not None:
            result = self.cache_data[key]
        return result
