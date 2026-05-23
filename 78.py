class Solution:
    def subsets(self, nums: List[int]):
        res = []

        def dfs(index, curr):
        
            if index == len(nums):
                res.append(curr[:])
                return

            
            curr.append(nums[index])
            dfs(index + 1, curr)

           
            curr.pop()

         
            dfs(index + 1, curr)

        dfs(0, [])
        return res
      
