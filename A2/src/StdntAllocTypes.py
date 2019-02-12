## @file StdntAllocTypes.py
#  @author Shunbo Cui
#  @brief StdntAllocTypes
#  @date 11/2/2019
from enum import Enum
from collections import namedtuple


## @An abstract data type that represents gender type
class GenT(Enum):
    male = 0
    female = 1


## @An abstract data type that represents departments
class DeptT(Enum):
    civil = 0
    chemical = 1
    electrical = 2
    mechanical = 3
    software = 4
    materials = 5
    engphys = 6


SInfoT = namedtuple("SInfoT", ["fname", "lname", "gender", "gpa", "choices", "freechoice"])
