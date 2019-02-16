##  @file SeqADT.py
#   @author Mengxi (William) Lei, leim5
#   @date Created 2019/02/05
#   @date Last modified 2019/02/09
#   @brief ADT for a sequence (list)


##  @brief Takes a sequence and manipulate it
class SeqADT:

    ##  @brief Construct the object, set count to 0 and sequence to input
    #   @param seq sequence of the type of the class
    #   @return object of SeqADT
    def __init__(self, seq):
        self.count = 0
        self.sequence = seq

    ##  @brief Reset the count to 0
    def start(self):
        self.count = 0

    ##  @brief Return the next item in the sequence
    #   @return next item in the sequence
    #   @throws StopIteration Reached the end of the array, no more item in the sequence
    def next(self):
        if (self.end()):
            raise StopIteration
        else:
            self.count += 1
            return self.sequence[self.count - 1]

    ##  @brief Check if at the end of the sequence
    #   @return boolean state whether the end of the sequence have been reached
    def end(self):
        if (self.count >= len(self.sequence)):
            return True
        else:
            return False
