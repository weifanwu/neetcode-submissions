class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        if sum(matchsticks) % 4 != 0:
            return False
    
        record = [0] * 4

        def dfs(index):
            if index == len(matchsticks):
                return record[0] == record[1] == record[2] == record[3]
            for side in range(4):
                record[side] += matchsticks[index]
                if record[side] > (sum(matchsticks) // 4):
                    record[side] -= matchsticks[index]
                    continue
                if dfs(index + 1):
                    return True
                record[side] -= matchsticks[index]
            return False

        return dfs(0)
