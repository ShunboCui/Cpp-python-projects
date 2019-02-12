from StdntAllocTypes import*
from SALst import*
from DCapALst import*
from SeqADT import*


def load_stdnt_data(s):
    f = open(s, "r", -1, "utf-8-sig")
    SALst.init()
    for line in f.readlines():
        v = line.strip().split(',')
        if v[3] == "male":
            gen = GenT.male
        else:
            gen = GenT.female
        sinfo1 = SInfoT(v[1], v[2], gen, float(v[4]), SeqADT(v[5]), v[6] == str(True))
        SALst.add(v[0], sinfo1)
    f.close()


def load_dcap_data(s):
    f = open(s, "r", -1, "utf-8-sig")
    DCapALst.init()
    for line in f.readlines():
        v = line.strip().split(',')
        if v[0] == "civil":
            dept = DeptT.civil
        elif v[0] == "chemical":
            dept = DeptT.chemical
        elif v[0] == "electrical":
            dept = DeptT.electrical
        elif v[0] == "mechanical":
            dept = DeptT.mechanical
        elif v[0] == "software":
            dept = DeptT.software
        elif v[0] == "materials":
            dept = DeptT.materials
        elif v[0] == "engphys":
            dept = DeptT.engphys
        SALst.add(dept, v[1])
    f.close()
