
from narwhals import List



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # i is passed again because the same number can be reused
                backtrack(i, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result