from collections import deque

from evaluation import test_longest_subarray_with_max_difference

def longest_max_difference(seq, limit):
    class IndexValue:
        def __init__(self, index, value):
            self.index = index
            self.value = value

        def __str__(self):
            return str(self.value) + ', ' + str(self.index)

    curr_min, curr_max = seq[0], seq[0]
    tracker = deque()
    tracker.append(IndexValue(0, seq[0]))
    curr_longest = 1
    for ix, val in enumerate(seq):
        if val > curr_max or val < curr_min:
            tracker.append(IndexValue(ix, val))
            if val > curr_max:
                curr_max = val
                updated_max = True
            else:
                curr_min = val
                updated_max = False
            # Check criterion
            if curr_max - curr_min > limit:
                # Update longest if necessary
                curr_longest = max(curr_longest, ix - tracker[0].index)
                # Delete items from left
                while abs(tracker[0].value - tracker[-1].value) > limit:
                    popped = tracker.popleft()
                # Update max and min
                if updated_max:
                    curr_min = tracker[0].value
                else:
                    curr_max = tracker[0].value
    # Check again at end
    return max(curr_longest, (ix - tracker[0].index) + 1)


if __name__ == '__main__':
    test_longest_subarray_with_max_difference(longest_max_difference)
