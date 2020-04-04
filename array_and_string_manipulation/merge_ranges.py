def merge_ranges(meetings):
    # create a new copy of the meetings and sort it in the process
    meetings = sorted(meetings)
    # initialize a variable ret to an empty list
    ret = []
    # initialize variables start and end to the intergers
    # in the first tuple in meetings
    start, end = meetings[0]
    # loop through meetings
    for index in range(1, len(meetings)):
        # compare end to the start time of current meeting
        # if end is greater than or equal to start time
        if end >= meetings[index][0]:
            # set end to the end time of current meeting
            end = meetings[index][1]
        # otherwise, if end is less than start time
        else:
            # append start time and end to ret as a tuple
            ret.append((start, end))
            # set start and end to the start and end times of next meeting
            start, end = meetings[index]
    # add the start and end time range to ret
    ret.append((start, end))
    # return ret
    return ret

print(merge_ranges([(1, 3), (2, 4)]))
print(merge_ranges([(5, 6), (6, 8)]))