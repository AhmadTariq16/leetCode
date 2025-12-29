"""217. Contains Duplicate: 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #nums_sorted = sorted(nums)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False


def main():
    input = [1, 2, 3, 1]
    solution = Solution()
    result = solution.containsDuplicate(input)
    print(result)


if __name__ == "__main__":
    main()


"""Recommended Solution:

len(nums)!=len(set(nums))

"""