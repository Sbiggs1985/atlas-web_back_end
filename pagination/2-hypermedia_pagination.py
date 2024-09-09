#!/usr/bin/env python3
"""Import CSV, MATH, and List."""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing the start and end indices for pagination."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """My init method."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page from the dataset."""
        """Code Below"""
        # Ensure that 'page' and 'page_size' are positive integers
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        pages = []
        if start >= len(self.dataset()):
            return pages
        pages = self.dataset()


    def get_hyper(self, page: int = 1, page_size: int = 10) ->\
        Dict[str, Union[int, List[List], None]]:
            data = self.get_page(page, page_size)
        
        # Total number of items
        total_items = len(self.dataset())
        # Calculate total number of pages
        total_pages = math.ceil(total_items / page_size)
        
        # Determine next page and previous page
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        
        # Return dictionary with pagination metadata and data
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }