#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = list(reader)
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """Deletion-resilient hypermedia pagination.

        Args:
            index (int): pagination index.
            page_size (int): pagination page size.

        Retunrs:
            a dict.
        """
        data = self.indexed_dataset()
        assert index < len(data.keys())
        sorted_keys = sorted(data.keys())
        if not index:
            index = 0
        paged_keys = [key for key in sorted_keys
                      if index <= key][:2]
        paged_data = [data[key] for key in paged_keys]
        next_index = sorted_keys.index(max(paged_keys)) + 1
        return {
                "index": index,
                "next_index": sorted_keys[next_index]
                if next_index < len(sorted_keys) else None,
                "page_size": len(paged_data),
                "data": paged_data
            }
