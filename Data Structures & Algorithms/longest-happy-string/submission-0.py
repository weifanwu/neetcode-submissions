class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = [[-count, value] for (count, value) in [(a, 'a'), (b, 'b'), (c, 'c') ]if count != 0]
        heapq.heapify(maxHeap)
        res = ""

        while maxHeap:
            currentMax = heapq.heappop(maxHeap)
            length = len(res)
            if length >= 2 and res[length - 1] == currentMax[1] and res[length - 2] == currentMax[1]:
                if maxHeap:
                    nextMax = heapq.heappop(maxHeap)
                    res += nextMax[1]
                    nextMax[0] += 1
                    if nextMax[0] < 0:
                        heapq.heappush(maxHeap, nextMax)
                    heapq.heappush(maxHeap, currentMax)
                else:
                    return res
            else:
                res += currentMax[1]
                currentMax[0] += 1
                if currentMax[0] < 0:
                    heapq.heappush(maxHeap, currentMax)
        return res