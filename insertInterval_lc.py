'''

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Accepted
176,760
Submissions
566,229

'''


incomplete.
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        p,q=newInterval
        startFound=False
        endFound=False
        for i in range(len(intervals)):

            if  startFound==False and intervals[i][0]<=p:
                start = i
                startFound= True
            if endFound==False and intervals[i][1]>=q:
                end=i
                endFound=True
            if startFound and endFound:
                break
        
        newInt= [ intervals[start][0], intervals[end][1] ]
        return intervals[:start]+[newInt] + intervals[end+1:]


s=Solution()

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

intervals = s.insert(intervals, newInterval)

print(intervals)
        