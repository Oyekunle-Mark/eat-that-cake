"""
my_rectangle = {

    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,

}
"""


def find_overlap(point1, length1, point2, length2):
    # get the highest_start_point as the max of point1 and point2
    highest_start_point = max(point1, point2)
    # get the lowest_end_point as the min of point1 plus length1
    # and point2 plus length2
    lowest_end_point = min(point1 + length1, point2 + length2)
    # if highest_start_point greater than or equal to lowest_end_point
    if highest_start_point >= lowest_end_point:
        # return a tuple of two Nones
        return (None, None)
    # set overlap_length to the difference between
    # highest_start_point and lowest_end_point
    overlap_length = highest_start_point - lowest_end_point
    # return a tuple of highest_start_point and overlap_length
    return (highest_start_point,  overlap_length)


def find_rectangular_overlap(rect1, rect2):
    # initialize left_x and width by destructuring the return value of
    # find_overlap passing in left_x and width of rect1 and rect2
    # initialize bottom_y and height by destructuring the return value of
    # find_overlap passing in bottom_y and height of rect1 and rect2
    # if left_x and bottom_y are None
        # return an object with None for all required properties
    # return an object with with the return values of find_overlap
    pass
