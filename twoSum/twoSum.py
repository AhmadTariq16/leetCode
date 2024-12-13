''' 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. '''


class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        final_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if ((nums[i] + nums[j]) == target):
                    final_list.append(i)
                    final_list.append(j)
        return final_list

def main():
    nums = [2, 7, 11, 15]
    target = 9

    twoSum = Solution()
    final_list = twoSum.twoSum(nums, target)
    print(final_list)

if __name__ == '__main__':
    main()


