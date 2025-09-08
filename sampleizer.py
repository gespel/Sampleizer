from modules import sine
from modules import randosine


class Sampleizer:
    def __init__(self, name):
        self.samples = []
        self.out_string = f"float {name}[] = {{"

    def add_sample(self, sample):
        self.out_string += f"{sample}, "
        self.samples.append(sample)

    def get_definition(self):
        out = self.out_string[:-2]
        out += "};"
        return out

    def get_samples(self):
        return self.samples

#s = Sampleizer("randosineOne")
#si = sine.Sine(10.0, 48000.0)
#rs = randosine.RandoSine(10, 48000.0, 1)
#for i in range(4800):
#    s.add_sample(rs.get_sample())

#s.visualize()
#print(s.get_definition())
        
