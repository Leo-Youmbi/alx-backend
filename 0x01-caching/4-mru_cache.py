#!/usr/bin/env python3
""" MRUCache module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Represents an object that allows storimng and
    retrieving items from a dictionary with a RU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.most_recentkeys_used = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if None in (key, item):
            return

        if len(self.cache_data) >= self.MAX_ITEMS and \
                key not in self.most_recentkeys_used:

            # Discard the most recently used item (LRU)
            mru_key = self.most_recentkeys_used.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")
        else:

            if key in self.most_recentkeys_used:
                self.most_recentkeys_used.remove(key)

        self.cache_data[key] = item
        self.most_recentkeys_used.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys() and key is not None:
            # Update most_recentkeys_used to mark the key as recently used
            self.most_recentkeys_used.remove(key)
            self.most_recentkeys_used.append(key)
            return self.cache_data[key]

        return None
