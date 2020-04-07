def sort_scores(unsorted_scores, highest_possible_score):
    # initialize a new list score_count to the size of highest_possible_score plus one
    score_count = [None] * (highest_possible_score + 1)
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
    # loop through every index of score_count backwards
    for index in range(len(score_count), -1, -1):
        # if score_count[index] is not None:
        if score_count[index] is not None:
            # append index to sorted_scores score_count[index] number of times
            for _ in range(score_count[index]):
                sorted_scores.append(index)
    # return sorted_scores
    return sorted_scores
