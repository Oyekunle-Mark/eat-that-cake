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
        if score_count[index - 1] is not None:
            # append index to sorted_scores score_count[index] number of times
            for _ in range(score_count[index - 1]):
                sorted_scores.append(index - 1)
    # return sorted_scores
    return sorted_scores


print(sort_scores([37, 89, 41, 65, 91, 53], 100))
print(sort_scores([20, 10, 30, 30, 10, 20], 100))
