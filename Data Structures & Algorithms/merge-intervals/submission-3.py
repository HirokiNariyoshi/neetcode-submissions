class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by first element
        intervals.sort()

        output = []
        output.append(intervals[0])
        
        for i in range(len(intervals) - 1):
            # there is overlap -> prev_end >= current_start
            if output[-1][1] >= intervals[i+1][0]:
                # stretch the stored interval to cover current end
                output[-1][1] = max(output[-1][1], intervals[i+1][1])
            else:
                # interval is good to add to output
                output.append(intervals[i+1])

        return output