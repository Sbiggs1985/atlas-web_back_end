#!/usr/bin/env python3
"""hypermedia pagination
"""
import csv
import math
from typing import List, Tuple, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Codebase to follow."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """We are returning a Tuple with a start index and an end index.

        We have providedthe args.

        Returning start index and end index.
        """
        end: int = page * page_size
        start: int = 0
        for _ in range(page - 1):
            start += page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Assigning the values."""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        if end > len(dataset):
            return []
        return [list(dataset[row]) for row in range(start, end)]

    def get_hyper(self, page: int = 1, page_size: int = 10) ->\
            Dict[str, Union[List[List], None, int]]:
        """Creating the methods for arguments."""

        data: List = self.get_page(page, page_size)
        size_dataset: int = len(self.dataset())
        total_pages = math.ceil(size_dataset / page_size)
        prev_page = None if page - 1 == 0 else page - 1
        next_page = None if page + 1 > size_dataset or data == [] else page + 1
        page_size = 0 if data == [] else page_size

        pagination_info: Dict = {'page_size': page_size,
                                 'page': page,
                                 'data': data,
                                 'next_page': next_page,
                                 'prev_page': prev_page,
                                 'total_pages': total_pages}

        return pagination_info
