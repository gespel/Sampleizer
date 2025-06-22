import sine

class Sampleizer:
    def __init__(self, name):
        self.samples = []
        self.out_string = f"float {name}[] = {{"

    def add_sample(self, sample):
        self.out_string += f"{sample}, "

    def get_definition(self):
        out = self.out_string[:-2]
        out += "};"
        return out

s = Sampleizer("sine")
si = sine.Sine(10.0, 48000.0)
for i in range(4800):
    s.add_sample(si.get_sample())
print(s.get_definition())
        
