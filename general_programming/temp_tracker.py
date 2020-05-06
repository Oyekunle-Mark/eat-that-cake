class TempTracker(object):
    def __init__(self):
        # initialize max_temp and min_temp to negative and positive infinities
        self.max_temp = float('-inf')
        self.min_temp = float('inf')
        # initialize mean, sum_so_far and count to zero
        self.mean, self.sum_so_far, self.count = 0, 0, 0
        # initialize mode to 
        # since the temperature range is 0..110
        # a list can be used to keep track of count each temperature integer

    def insert(self, temperature):
        # increment count by one
        self.count += 1
        # add temperature to  sum_so_far
        self.sum_so_far += temperature
        # set mean to the division of sum_so_far and count
        self.mean = self.sum_so_far / self.count

        # increment number at index temperature of temp_range
        # if index temperature of temp_range is greater than mode
            # set mode to temperature

        # if temperature is greater than max_temp
        if temperature > self.max_temp:
            # set max_temp to temperature
            self.max_temp = temperature
        # otherwise if temperature is lower than min_temp
        elif temperature < self.min_temp:
            # set min_temp to temperature
            self.min_temp = temperature

    def get_max(self):
        # return max_temp
        return self.max_temp

    def get_min(self):
        # return min_temp
        return self.min_temp

    def get_mean(self):
        # return mean
        return self.mean

    def get_mode(self):
        # return mode
        pass
