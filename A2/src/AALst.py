class AALst:

    s = []

    @staticmethod
    def init():
        AALst.s = []

    @staticmethod
    def add_stdnt(dep, m):
        tup = (dep, m)
        AALst.s.append(tup)

    @staticmethod
    def lst_alloc(d):
        for tup1 in AALst.s:
            if d in tup1:
                return(tup1[1])

    @staticmethod
    def num_alloc(d):
        for tup1 in AALst.s:
            if d in tup1:
                return(len(tup1[1]))
        return 0
