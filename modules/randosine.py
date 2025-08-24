import random

from modules.sawtooth import Sawtooth
from modules.sine import Sine
from modules.square import Square


class RandoSine:
    def __init__(self, freq, sample_rate, num_oscillators):
        self.freq = freq
        self.sample_rate = sample_rate
        self.oscs = []
        for x in range(0, num_oscillators):
            self.oscs.append(Square(freq // 2 * random.randint(1, 8), sample_rate))
            self.oscs.append(Sawtooth(freq // 2 * random.randint(1, 8), sample_rate))
            self.oscs.append(Sine(freq // 2 * random.randint(1, 8), sample_rate))
    def get_sample(self):
        out = 0.0
        for osc in self.oscs:
            out += osc.get_sample()
        out /= len(self.oscs)
        return round(out, 8)