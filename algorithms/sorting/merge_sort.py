"""Module with the implementation of the MergeSort algorithm."""

from typing import List

from .sort import Sort


class BaseMergeSort(Sort):
    """Base Merge Sort class."""

    def _merge(self, left: List, right: List) -> List:
        merged = []
        left_idx = 0
        right_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if self._comp_func(left[left_idx], right[right_idx]):
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1

        while left_idx < len(left):
            merged.append(left[left_idx])
            left_idx += 1

        while right_idx < len(right):
            merged.append(right[right_idx])
            right_idx += 1

        return merged


class RecursiveMergeSort(BaseMergeSort):
    """Class that represents a recursive MergeSort implementation."""

    def _sort(self, items: List) -> List:
        if len(items) <= 1:
            return items

        left = items[: len(items) // 2]
        right = items[len(items) // 2 :]

        left = self._sort(left)
        right = self._sort(right)

        return self._merge(left, right)


class IterativeMergeSort(BaseMergeSort):
    """Class that represents an iterative MergeSort implementation."""

    def _sort(self, items: List) -> List:

        sorted_items = items.copy()
        chunk_size = 1
        while chunk_size < len(sorted_items):

            i = 0
            while i < len(sorted_items):
                mid = i + chunk_size
                j = min(i + 2 * chunk_size, len(sorted_items))
                sorted_items[i:j] = self._merge(
                    sorted_items[i:mid], sorted_items[mid:j]
                )

                i += chunk_size * 2

            chunk_size *= 2

        return sorted_items
