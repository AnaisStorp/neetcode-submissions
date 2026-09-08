class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of = {n: i for i, n in enumerate(nums)}
        for i , n in enumerate(nums):
            j = index_of.get(target-n)
            if j is not None and j != i:
                return [i, j]
        return []