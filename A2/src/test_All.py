from StdntAllocTypes import *
from SeqADT import *
from DCapALst import *
from AALst import *
from SALst import *

from pytest import *

class TestSALst:
    def SALsttest1(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        assert SALst.elm("stdnt1") == True

    def SALsttest2(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        SALst.remove("stdnt1")
        assert SALst.elm("stdnt1") == False

    def SALsttest3(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        assert SALst.info("stdnt1") == SInfoT(fname='first', lname='last', gender=<GenT.male: 0>, gpa=12.0, choices=<SeqADT.SeqADT object at 0x000002AC29F1CC88>, freechoice=True)

    def SALsttest4(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        sinfo2 = SInfoT("first2", "last2", GenT.female, 8.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == ['stdnt1', 'stdnt2']
