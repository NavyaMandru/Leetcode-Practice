# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Time complexity - O(n)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)<=1:
            return intervals
        
        result = []
        intervals.sort()
        newInt = intervals[0]
        result.append(newInt)

        for Int in intervals:
            if newInt[1] >= Int[0]:
                newInt[1] = max(newInt[1],Int[1])

            else:
                newInt = Int
                result.append(newInt)

                
        return result
        
