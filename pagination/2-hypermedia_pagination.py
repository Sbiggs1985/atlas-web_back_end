#!/usr/bin/env python3
"""Hypermedia pagination."""
import math
from typing import List, Dict, Any, Optional


class Server:
    def __init__(self, dataset: List[List[Any]]):
        self.__dataset = dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[Any]]:
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        if start_index >= len(self.__dataset):
            return []

        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        data = self.get_page(page, page_size)
        total_data = len(self.__dataset)
        total_pages = math.ceil(total_data / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
