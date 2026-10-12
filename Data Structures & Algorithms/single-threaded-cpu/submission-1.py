class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = []
        for i in range(0, len(tasks)):
            tasks[i].append(i)
        
        availableTasks = []

        heapq.heapify(availableTasks)
        tasks.sort(key=lambda x : x[0])

        currentTask = 0
        currentTime = tasks[currentTask][0]

        while currentTask < len(tasks):
            task = tasks[currentTask]
            if task[0] <= currentTime or not availableTasks:
                heapq.heappush(availableTasks, [task[1], task[2]])
                currentTask += 1
                continue
            if availableTasks:
                available = heapq.heappop(availableTasks)
                currentTime += available[0]
                result.append(available[1])

        while availableTasks:
            restTask = heapq.heappop(availableTasks)
            result.append(restTask[1])

        return result
