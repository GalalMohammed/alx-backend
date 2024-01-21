#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines LRUCache class.

Example:
    my_cache = LRUCache()

"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A caching system."""

    def __init__(self):
        """__init__ method."""
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if item and key:
            self.cache_data[key] = item
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)
            if len(self.lru) > BaseCaching.MAX_ITEMS:
                discarded_key = self.lru.pop(0)
                print("DISCARD:", discarded_key)
                del self.cache_data[discarded_key]

    def get(self, key):
        """ Get an item by key
        """
        if key in self.lru:
            self.lru.remove(key)
            self.lru.append(key)
        return self.cache_data.get(key)
