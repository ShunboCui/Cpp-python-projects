class DCapALst:

    s = []

    @staticmethod
    def init():
        DCapALst.s = []

    @staticmethod
    def add(d, n):
        tup = (d, n)
        for tup1 in DCapALst.s:
            if d in tup1:
                raise KeyError("tuple already in set")
        DCapALst.s.append(tup)

    @staticmethod
    def remove(d):
        for tup1 in DCapALst.s:
            if d not in tup1:
                continue
            raise KeyError("tuple not in set")
        for tup1 in DCapALst.s:
            if d in tup1:
                DCapALst.s.remove(tup1)

    @staticmethod
    def elm(d):
        for tup1 in DCapALst.s:
            if d in tup1:
                return True
        return False

    @staticmethod
    def capacity(d):
        for tup1 in DCapALst.s:
            if d == tup1[0]:
                return tup1[1]
        raise KeyError("tuple not in set")


class KeyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
