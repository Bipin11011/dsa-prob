class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = []

        for i in range(len(nums)):
            if nums[i] != val:
                s.append(nums[i])

        nums[:] = s

        return len(nums)
