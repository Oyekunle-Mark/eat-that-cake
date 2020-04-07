def sort_scores(unsorted_scores, highest_possible_score):
    # initialize a new list score_count to the size of highest_possible_score plus one
    score_count = [None] * highest_possible_score + 1
    # initialize sorted_scores to an empty list
    sorted_scores = []
    # loop through every score in unsorted_scores
    for score in unsorted_scores:
        # if item at score index of score_count is not None
        if score_count[score] is not None:
            # increment the item
            score_count[score] += 1
        # otherwise,
        else:
            # set the score index of score_count to one
            score_count[score] = 1
    # loop through every count in score_count:
    for index, count in enumerate(score_count):
        # if current count is not None
        if count is not None:
            # append the current index to sorted_scores count number of times
            for _ in range(count):
                sorted_scores.append(count)
    # return sorted_scores
    return sorted_scores
