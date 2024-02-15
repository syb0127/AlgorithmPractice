class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        curr_interval = intervals[0]
        final_array = []
	
        for i in range(1,len(intervals)):
            if intervals[i][0] <= curr_interval[1]:
                curr_interval = [min(intervals[i][0], curr_interval[0]), max(intervals[i][1], curr_interval[1])]
            else:
                final_array.append(curr_interval)
                curr_interval = intervals[i]
        final_array.append(curr_interval)
        return final_array