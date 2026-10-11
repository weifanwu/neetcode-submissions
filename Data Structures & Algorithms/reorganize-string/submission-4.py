class Solution:
    def reorganizeString(self, s: str) -> str:

        c = Counter(s)
        maxHeap = [[-value, key] for [key, value] in c.items()]
        prev = None
        heapq.heapify(maxHeap)
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            count, character = heapq.heappop(maxHeap)
            res += character
            count += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if count != 0:
                prev = [count, character]

        return res