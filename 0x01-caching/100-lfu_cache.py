#!/usr/bin/env python3
""" LFUCache module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Represents an object that allows storing and
    retrieving items from a dictionary with a LFU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.least_keys_used = []
        self.data_freq = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if None in (key, item):
            return

        if len(self.cache_data) >= self.MAX_ITEMS and \
                key not in self.least_keys_used:
            data_freq = self.data_freq

            min_freq = min(data_freq.values())
            least_frequent_keys = [
                k for k, v in data_freq.items() if v == min_freq
                ]

            if len(least_frequent_keys) <= 1:
                del_key = least_frequent_keys[0]
            else:
                for k in self.least_keys_used:
                    if k in least_frequent_keys:
                        del_key = k
                        break

            del self.data_freq[del_key]
            self.least_keys_used.remove(del_key)
            del self.cache_data[del_key]
            print(f"DISCARD: {del_key}")
        else:

            if key in self.least_keys_used:
                self.least_keys_used.remove(key)

        if key in self.cache_data:
            self.data_freq[key] += 1
        else:
            self.data_freq[key] = 1

        self.cache_data[key] = item
        self.least_keys_used.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys() and key is not None:
            # Update least_keys_used to mark the key as recently used
            self.data_freq[key] += 1
            self.least_keys_used.remove(key)
            self.least_keys_used.append(key)
            return self.cache_data[key]

        return None
