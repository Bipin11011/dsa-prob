class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        res = []

        def dfs(index, curr, total):
       
            if total == target:
                res.append(curr[:])
                return

            if index >= len(candidates) or total > target:
                return

            curr.append(candidates[index])
            dfs(index, curr, total + candidates[index])  
            curr.pop()

           
            dfs(index + 1, curr, total)

        dfs(0, [], 0)
        return res
