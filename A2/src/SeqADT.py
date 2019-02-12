## @file SeqADT.py
#  @author Shunbo Cui
#  @brief SeqADT
#  @date 11/2/2019


## @An abstract data type that represents a sequence
class SeqADT:
    def __init__(self, x):
        self.s = x
        self.i = 0

## @brief SeqADT constructor
    def start(self):
        self.i = 0

## @brief moves to next element in the sequence
#  @return the pointer of the location of the element
    def next(self):
        if self.i >= len(self.s):
            raise StopIteration("Sequence length exceeded")
        temp = self.s[self.i]
        self.i = self.i + 1
        return temp

    def end(self):
        return self.i >= len(self.s)


## @brief defining the exception
#  @return the value of the string
class StopIteration(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
