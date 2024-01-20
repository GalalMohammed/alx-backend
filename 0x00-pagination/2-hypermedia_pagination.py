#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines index_range function.

Example:
    res = index_range(page=3, page_size=15)

"""


import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = list(reader)
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Paginate the dataset.

        Args:
            page (int): page of dataset.
            page_size (int): size of page.

        Returns:
            list of rows.
        """
        self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        if start >= len(self.__dataset) or end > len(self.__dataset):
            return []
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Hypermedia pagination.

        Args:
            page (int): pagination page.
            page_size (int): pagination page size.

        Returns:
            a dictionary.

        """
        data = self.get_page(page, page_size)
        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": page + 1
                if page * page_size < len(self.__dataset) else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": math.ceil(len(self.__dataset) / page_size)
            }
