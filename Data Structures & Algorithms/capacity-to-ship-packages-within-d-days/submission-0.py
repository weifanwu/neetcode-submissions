class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(cap):
            ships, currentCap = 1, cap
            for weight in weights:
                if currentCap - weight < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currentCap = cap
                currentCap -= weight

            return True
        
        left, right = max(weights), sum(weights)
        result = right
        while left <= right:
            capacity = (left + right) // 2
            if canShip(capacity):
                result = min(result, capacity)
                right = capacity - 1
            else:
                left = capacity + 1
        return result;



