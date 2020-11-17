from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Solution 2
        [MEMO] Chronological sort, brilliant!!!
        Separate apart start and end, basically we just need to know when a meeting ends, but we don't care which meeting ends
        """
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        starts.sort()
        ends.sort()

        i, j = 0, 0
        max_rooms = 0
        rooms = 0
        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                rooms += 1
                i += 1

                if rooms > max_rooms:
                    max_rooms = rooms
            else:
                rooms -= 1
                j += 1
        return max_rooms

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Draft 1
        Keep track of running meetings, beats 43%
        Can increase to 68% if just store end times to runnings
        [MEMO] Can change runnings to a min_heap to further reduce search time
        """
        if not intervals:
            return 0

        intervals.sort()
        runnings = []
        max_rooms = 0
        for meeting in intervals:
            if not runnings:
                runnings.append(meeting)
            else:
                runnings = [running for running in runnings if running[1] > meeting[0]]
                runnings.append(meeting)

            # update max rooms
            rooms = len(runnings)
            if rooms > max_rooms:
                max_rooms = rooms
        return max_rooms
