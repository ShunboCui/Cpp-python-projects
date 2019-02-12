## @file AALst.py
#  @author Shunbo Cui
#  @brief AALst
#  @date 11/2/2019


## @An abstract data type that represents allocation association list
class AALst:

    s = []

    ## @brief constructor of the data type
    @staticmethod
    def init():
        AALst.s = []

    ## @brief appending elements to the association list
    @staticmethod
    def add_stdnt(dep, m):
        tup = (dep, m)
        AALst.s.append(tup)

    ## @brief get the list in the tuple
    #  @return the list related to input d
    @staticmethod
    def lst_alloc(d):
        for tup1 in AALst.s:
            if d in tup1:
                return(tup1[1])

    ## @brief get the length of list in the tuple
    #  @return the length of list related to input d
    @staticmethod
    def num_alloc(d):
        for tup1 in AALst.s:
            if d in tup1:
                return(len(tup1[1]))
        return 0
