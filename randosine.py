import random

import sine

class RandoSine:
    def __init__(self, freq, sample_rate, num_oscillators):
        self.freq = freq
        self.sample_rate = sample_rate
        self.oscs = [sine.Sine(freq//2 * random.randint(1, 8), sample_rate) for i in range(0, num_oscillators)]

    def get_sample(self):
        out = 0.0
        for osc in self.oscs:
            out += osc.get_sample()
        out /= len(self.oscs)
        return round(out, 8)