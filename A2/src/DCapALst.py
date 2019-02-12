## @file DCapALst.py
#  @author Shunbo Cui
#  @brief DCapALst
#  @date 11/2/2019


## @An abstract data type that represents Department capacity type
class DCapALst:

    s = []

    ## @brief constructor of the data type
    @staticmethod
    def init():
        DCapALst.s = []

    ## @brief appending elements to the departments list
    @staticmethod
    def add(d, n):
        tup = (d, n)
        for tup1 in DCapALst.s:
            if d in tup1:
                raise KeyError("tuple already in set")
        DCapALst.s.append(tup)

    ## @brief deleting elements in the departments list
    @staticmethod
    def remove(d):
        for tup1 in DCapALst.s:
            if d not in tup1:
                continue
            raise KeyError("tuple not in set")
        for tup1 in DCapALst.s:
            if d in tup1:
                DCapALst.s.remove(tup1)

    ## @brief check if element in the list
    #  @return the boolean value representing if exists
    @staticmethod
    def elm(d):
        for tup1 in DCapALst.s:
            if d in tup1:
                return True
        return False

    ## @brief check the capacity of the department
    #  @return the interger of the capacity
    @staticmethod
    def capacity(d):
        for tup1 in DCapALst.s:
            if d == tup1[0]:
                return tup1[1]
        raise KeyError("tuple not in set")


## @brief defining the exception
#  @return the value of the string
class KeyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
