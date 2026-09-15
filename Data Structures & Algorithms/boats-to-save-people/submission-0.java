class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int first = 0;
        int second = people.length - 1;
        int result = 0;

        while (second >= first) {
            if (second == first) {
                result++;
                return result;
            } else if (people[first] + people[second] <= limit) {
                result++;
                first++;
                second--;
            } else {
                result++;
                second--;
            }
        }

        return result;

    }
}