class SeqADT:
    def __init__(self, x):
        self.s = x
        self.i = 0

    def start(self):
        self.i = 0

    def next(self):
        self.i = self.i + 1
        if self.i >= len(self.s):
            raise StopIteration("Sequence length exceeded")
        return self.s[self.i]

    def end(self):
        return self.i >= len(self.s)
