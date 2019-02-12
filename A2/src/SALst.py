## @file SALst.py
#  @author Shunbo Cui
#  @brief SALst
#  @date 11/2/2019
from StdntAllocTypes import*
from AALst import*
from DCapALst import*


## @An abstract data type that do operations to the data
class SALst:

    s = []

    ## @brief constructor of the data type
    @staticmethod
    def init():
        SALst.s = []

    ## @brief appending elements to the student list
    @staticmethod
    def add(m, i):
        tup = (m, i)
        for tup1 in SALst.s:
            if m in tup1:
                raise KeyError("tuple already in set")
        SALst.s.append(tup)

    ## @brief removing elements in the student list
    @staticmethod
    def remove(m):
        for tup1 in SALst.s:
            if m not in tup1:
                continue
            raise KeyError("tuple not in set")
        for tup1 in SALst.s:
            if m in tup1:
                SALst.s.remove(tup1)

    ## @brief check if element in the list
    #  @return the boolean representing if the element exists
    @staticmethod
    def elm(m):
        for tup1 in SALst.s:
            if m in tup1[1]:
                return True
        return False

    ## @brief getting the information in the tuple
    #  @return the information of the student responding to the macid
    @staticmethod
    def info(m):
        for tup1 in SALst.s:
            if m in tup1:
                return tup1[1]
        raise ValueError("tuple not in set")

    ## @brief sorting the student list
    #  @return the sorted list of students
    @staticmethod
    def sort(f):
        L1 = []
        Lm = []
        for tup1 in SALst.s:
            if f(tup1[1]):
                L1.append(tup1)
        L2 = sorted(L1, key=lambda x: (x[1].gpa), reverse=True)
        for tup2 in L2:
            Lm.append(tup2[0])
        return Lm

    ## @brief calculating the average gpa in the list
    #  @return the float of the average gpa value
    @staticmethod
    def average(f):
        L3 = []
        sum = 0
        count = 0
        for tup1 in SALst.s:
            if f:
                print(f)
                L3.append(tup1)
        if L3 == []:
            raise ValueError("List is empty")
        for tup2 in L3:
            sum += tup2[1].gpa
            count += 1
        average = sum / count
        return average

    ## @brief allocate the students to departments
    @staticmethod
    def allocate():
        F = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in F:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)
        S = SALst.sort(lambda t: (not (t.freechoice)) and t.gpa >= 4.0)
        for m in S:
            ch = SALst.info(m).choices
            alloc = False
            while (not alloc) and (not ch.end()):
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if not alloc:
                raise RuntimeError("Run time error")


## @brief defining the exception
#  @return the value of the string
class ValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


## @brief defining the exception
#  @return the value of the string
class RuntimeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
