class DCapALst:

    s = set()

    @staticmethod
    def init():
        DCapALst.s = set()

    @staticmethod
    def add(d, n):
        tup = (d, n)
        for tup1 in DCapALst.s:
            if d in tup1:
                raise KeyError("tuple already in set")
        DCapALst.s = DCapALst.s.add(tup)

    @staticmethod
    def remove(d):
        for tup1 in DCapALst.s:
            if d in tup1:
                break
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
            if d in tup1:
                return tup1[1]
        raise KeyError("tuple not in set")
