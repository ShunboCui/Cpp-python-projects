from StdntAllocTypes import*
from AALst import*
from DCapALst import*


class SALst:

    s = []

    @staticmethod
    def init():
        SALst.s = []

    @staticmethod
    def add(m, i):
        tup = (m, i)
        for tup1 in SALst.s:
            if m in tup1:
                raise KeyError("tuple already in set")
        SALst.s.append(tup)

    @staticmethod
    def remove(m):
        for tup1 in SALst.s:
            if m not in tup1:
                continue
            raise KeyError("tuple not in set")
        for tup1 in SALst.s:
            if m in tup1:
                SALst.s.remove(tup1)

    @staticmethod
    def elm(m):
        for tup1 in SALst.s:
            if m in tup1:
                return True
        return False

    @staticmethod
    def info(m):
        for tup1 in SALst.s:
            if m in tup1:
                return tup1[1]
        raise ValueError("tuple not in set")

    @staticmethod
    def sort(f):
        L1 = []
        Lm = []
        for tup1 in SALst.s:
            if f:
                L1.append(tup1)
        L2 = sorted(L1, key=lambda x: (x[1].gpa), reverse=True)
        for tup2 in L2:
            Lm.append(tup2[0])
        return Lm

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

    @staticmethod
    def allocate():
        F = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in F:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)
        #S = SALst.sort(lambda t: not (t.freechoice) and t.gpa >= 4.0)
        S = []
        for m in S:
            ch = SALst.info(m).choices
            alloc = False
            while not alloc and not ch.end():
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if not alloc:
                raise RuntimeError("Run time error")


class ValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class RuntimeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
