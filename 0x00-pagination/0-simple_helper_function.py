#!/usr/bin/env python3
"""
Pagination helper function.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
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
