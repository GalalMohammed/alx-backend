#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines LIFOCache class.

Example:
    my_cache = LIFOCache()

"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system."""

    def __init__(self):
        """__init__ method."""
        super().__init__()
        self.lifo = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if item and key:
            self.cache_data[key] = item
            if key in self.lifo:
                self.lifo.remove(key)
            self.lifo.append(key)
            if len(self.lifo) > BaseCaching.MAX_ITEMS:
                discarded_key = self.lifo.pop(-2)
                print("DISCARD:", discarded_key)
                del self.cache_data[discarded_key]

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
