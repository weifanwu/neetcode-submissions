class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        first = 0
        second = len(people) - 1
        result = 0
        while (first <= second):
            if (first == second):
                result = result + 1;
                return result
            elif (people[first] + people[second] <= limit):
                result = result + 1
                first = first + 1
                second = second - 1
            else:
                result = result + 1;
                second = second - 1
        return result