class TempTracker(object):
    def __init__(self):
        # initialize max_temp and min_temp to None
        self.max_temp = None
        self.min_temp = None
        # initialize mean, sum_so_far and count to zero
        self.mean, self.sum_so_far, self.count = 0, 0, 0
        # initialize mode to zero
        self.mode = 0
        # since the temperature range is 0..110
        # a list can be used to keep track of count each temperature integer
        self.temp_frequency = [0] * 111

    def insert(self, temperature):
        # if self.max_temp and self.min_temp is None
        if self.max_temp is None and self.min_temp is None:
            # set both to temperature
            self.max_temp, self.min_temp = temperature

        # increment count by one
        self.count += 1
        # add temperature to  sum_so_far
        self.sum_so_far += temperature
        # set mean to the division of sum_so_far and count
        self.mean = self.sum_so_far / self.count

        # increment number at index temperature of temp_frequency
        self.temp_frequency[temperature] += 1
        # if index temperature of temp_frequency is greater than mode
        if self.temp_frequency[temperature] > self.mode:
            # set mode to temperature
            self.mode = temperature

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
        return self.mode
