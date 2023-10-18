from abc import ABC, abstractmethod

class BinarySearch(ABC):
    @abstractmethod
    def search(self, nums, target):
        pass

class BasicBinarySearch(BinarySearch):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

class LowerBoundBinarySearch(BinarySearch):
    def search(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

class UpperBoundBinarySearch(BinarySearch):
    def search(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left



# Example usage
basic_search = BasicBinarySearch()
lower_bound_search = LowerBoundBinarySearch()
upper_bound_search = UpperBoundBinarySearch()

nums = [1, 2, 2, 2, 3, 4, 5]
target = 2

print("Basic Binary Search Result:", basic_search.search(nums, target))
print("Lower Bound Binary Search Result:", lower_bound_search.search(nums, target))
print("Upper Bound Binary Search Result:", upper_bound_search.search(nums, target))
