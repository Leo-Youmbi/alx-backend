#!/usr/bin/env python3
"""Simple pagination sample.
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.

    Args:
        page (int): Page number
        page_size (int): Number of items per page

    Returns:
        Tuple: tuple containing start and end indices
    """
    # Calculate the start index
    start_index = (page - 1) * page_size

    # Calculate the end index
    end_index = start_index + page_size

    return start_index, end_index


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
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data

        Args:
            page (int, optional): Page Number. Defaults to 1.
            page_size (int, optional): Number of items per page.
                Defaults to 10.

        Returns:
            List[List]: Page of data
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        i_range = index_range(page, page_size)
        start_index, end_index = i_range
        dataset = self.dataset()
        result = []

        if dataset is not None and end_index < len(dataset):
            for i in range(start_index, end_index):
                result.append(dataset[i])
        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieves hyper information about a page.
        """
        dataset = self.dataset()
        start_index, end_index  = index_range(page, page_size)
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end_index < len(dataset) else None,
            'prev_page': page - 1 if start_index > 0 else None,
            'total_pages': total_pages
        }
