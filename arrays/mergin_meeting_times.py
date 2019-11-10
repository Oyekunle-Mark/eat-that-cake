def merge_ranges(meetings):
    # the input list of tuples might not be sorted, so sort it.
    meetings_list = sorted(meetings)
    # set the first meeting to an array of the first tuple in meetings
    ordered_meetings = [meetings_list[0]]
    # loop through the meeting for start and end times
    for start_time, end_time in meetings_list:
        # set the previous start and end times to the last item in the meeting array
        previous_start, previous_end = ordered_meetings[-1]
        # check if
        if previous_end >= start_time:
            if previous_end >= end_time:
                continue
            else:
                ordered_meetings[-1] = (previous_start, end_time)
        else:
            ordered_meetings.append((start_time, end_time))

    return ordered_meetings


print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(merge_ranges([(1, 2), (2, 3)]))
print(merge_ranges([(1, 5), (2, 3)]))
print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))
print(merge_ranges([(1, 3), (2, 4)]))
