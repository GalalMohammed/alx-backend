#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines MRUCache class.

Example:
    my_cache = MRUCache()

"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A caching system."""

    def __init__(self):
        """__init__ method."""
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if item and key:
            self.cache_data[key] = item
            if key in self.mru:
                self.mru.remove(key)
            self.mru.append(key)
            if len(self.mru) > BaseCaching.MAX_ITEMS:
                discarded_key = self.mru.pop(-2)
                print("DISCARD:", discarded_key)
                del self.cache_data[discarded_key]

    def get(self, key):
        """ Get an item by key
        """
        if key in self.mru:
            self.mru.remove(key)
            self.mru.append(key)
        return self.cache_data.get(key)
