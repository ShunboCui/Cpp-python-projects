from enum import Enum
from collections import namedtuple


class GenT(Enum):
    male = 0
    female = 1


class DeptT(Enum):
    civil = 0
    chemical = 1
    electrical = 2
    mechanical = 3
    software = 4
    materials = 5
    engphys = 6


SInfoT = namedtuple("SInfoT", ["fname", "lname", "gender", "gpa", "choices", "freechoice"])
