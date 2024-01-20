#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines index_range function.

Example:
    res = index_range(page=3, page_size=15)

"""


def index_range(page: int, page_size: int) -> tuple:
    """Compute the start index and the end index
    corresponding to the range of indexes
    to return in a list for those particular pagination parameters.

    Args:
        page (int): pagination page.
        page_size (int): pagination page size.

    Returns:
        a tuple of size two.

    """
    return ((page - 1) * page_size, page * page_size)
