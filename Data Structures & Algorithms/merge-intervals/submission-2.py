class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        output.append(intervals[0])

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # add prev interval to the current
                output[-1][1] = max(lastEnd, end)
            else:
                # interval fine as is
                output.append([start, end])
        return output