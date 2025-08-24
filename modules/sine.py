import math


class Sine:
    def __init__(self, freq, sample_rate):
        self.freq = freq
        self.phase = 0
        self.sample_rate = sample_rate

    def get_sample(self):
        self.phase += (self.freq / self.sample_rate) * math.pi * 2
        return round(float(math.sin(self.phase)), 8)
