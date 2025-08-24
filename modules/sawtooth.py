import math


class Sawtooth:
    def __init__(self, freq, sample_rate):
        self.freq = freq
        self.add = freq / sample_rate
        self.sample_rate = sample_rate
        self.out = 0

    def get_sample(self):
        if self.out > 1:
            self.out = -1
        self.out += self.add
        return self.out