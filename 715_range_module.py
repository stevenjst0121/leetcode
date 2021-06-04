import bisect


class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        """
        [MEMO] Use of bisect
        Also it turns out no need to worry about open/close
        When adding, can only be [open, close)
        When removing, in any situation, interval will still always be [open, close)
        Instead of using a list, could be faster using a double-linked list
        """
        bisect.insort_left(self.intervals, [left, right])

        new_interval = []
        for start, end in self.intervals:
            if not new_interval or new_interval[-1][1] < start:
                new_interval.append([start, end])
            else:
                new_interval[-1][1] = max(new_interval[-1][1], end)
        self.intervals = new_interval
        # print(self.intervals)

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.intervals:
            if left >= start and right <= end:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []
        for start, end in self.intervals:
            if right <= start or left >= end:
                # No intersection
                new_intervals.append([start, end])
            else:
                # Must have some intersection
                if left <= start:
                    # Left must be included
                    if right >= end:
                        # 100% included
                        continue
                    else:
                        new_intervals.append([right, end])
                else:
                    # Right must be included
                    new_intervals.append([start, left])
                    if right >= end:
                        continue
                    else:
                        new_intervals.append([right, end])
        self.intervals = new_intervals
        # print(self.intervals)