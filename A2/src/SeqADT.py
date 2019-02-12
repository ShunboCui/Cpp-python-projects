class SeqADT:
    def __init__(self, x):
        self.s = x
        self.i = 0

    def start(self):
        self.i = 0

    def next(self):
        if self.i >= len(self.s):
            raise StopIteration("Sequence length exceeded")
        temp = self.s[self.i]
        self.i = self.i + 1
        return temp

    def end(self):
        return self.i >= len(self.s)


class StopIteration(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
