#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines FIFOCache class.

Example:
    my_cache = FIFOCache()

"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system."""

    def __init__(self):
        """__init__ method."""
        super().__init__()
        self.fifo = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if item and key:
            self.cache_data[key] = item
            self.fifo.append(key)
            if len(self.fifo) > BaseCaching.MAX_ITEMS:
                discarded_key = self.fifo.pop(0)
                print("DISCARD:", discarded_key)
                del self.cache_data[discarded_key]

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
