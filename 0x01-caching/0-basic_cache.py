#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines BasicCache class.

Example:
    my_cache = BasicCache()

"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system"""

    def put(self, key, item):
        """Assign to the dictionary.

        Args:
            key (object): the key.
            item (object): the value.

        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get the value.

        Args:
            key (object): the key.

        Returns:
            the value.

        """
        return self.cache_data.get(key)
