##  @file SALst.py
#   @author Mengxi (William) Lei, leim5
#   @date Created 2019/02/07
#   @date Last modified 2019/02/09
#   @brief Class for the allocation of student

from operator import itemgetter
from StdntAllocTypes import *
from AALst import *
from DCapALst import *


##  @brief Class for the allocation of student
class SALst:

    seq = None

    ##  @brief Construct the object, initialize a empty dictionary
    @staticmethod
    def init():
        SALst.seq = {}

    ##  @brief Add the student to the dictionary
    #   @param macid student's macid
    #   @param info the student's information
    #   @throws KeyError student with the macid already in dictionary
    @staticmethod
    def add(macid, info):
        if SALst.elm(macid):
            raise KeyError
        else:
            SALst.seq[macid] = info

    ##  @brief Remove the student from the dictionary
    #   @param macid macid of student being removed
    #   @throws KeyError macid not in dictionary
    @staticmethod
    def remove(macid):
        if SALst.elm(macid):
            del SALst.seq[macid]
        else:
            raise KeyError

    ##  @brief Check if the element is inside the current dictionary
    #   @param macid macid being checked
    #   @return boolean state if the macid is in dictionary or not
    @staticmethod
    def elm(macid):
        if macid in SALst.seq:
            return True
        else:
            return False

    ##  @brief Retrieve the information of the student
    #   @param macid macid of student whose information is being retrieved
    #   @return the information of the student
    #   @throws ValueError macid not in dictionary
    @staticmethod
    def info(macid):
        if SALst.elm(macid):
            return SALst.seq[macid]
        else:
            raise ValueError

    ##  @brief Sort the students who satisfies the given condition is decreasing gpa
    #   @param condition condition of which students are being sorted
    #   @return list of student's macid sorted by gpa (decreasing order)
    @staticmethod
    def sort(condition):
        id_list = SALst.seq.keys()
        info_list = []
        list = []
        for element in id_list:
            if condition(SALst.seq[element]):
                info_list.append({"id": element, "grade": SALst.seq[element].gpa})
        info_list.sort(key=itemgetter("grade"), reverse=True)
        for item in info_list:
            list.append(item["id"])
        return list

    ##  @brief Return the average of the students that satisfies the given condition
    #   @param condition condition of which students are being used for calculation
    #   @return the average of the students
    #   @throws ValueError no student meet the condition
    @staticmethod
    def average(condition):
        id_list = SALst.seq.keys()
        grade = 0
        count = 0
        for element in id_list:
            if condition(SALst.seq[element]):
                grade += SALst.seq[element].gpa
                count += 1
        if count == 0:
            raise ValueError
        else:
            return (grade / count)

    ##  @brief Allocate students depend on freechoice, gpa and their choices
    #   @throws RuntimeError Student not allocated
    @staticmethod
    def allocate():
        AALst.init()
        sorted_student = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for element in sorted_student:
            choice_list = SALst.seq[element].choices
            AALst.add_stdnt(choice_list.next(), element)
        sorted_student = SALst.sort(lambda t: (not t.freechoice) and t.gpa >= 4.0)
        for element in sorted_student:
            choice_list = SALst.seq[element].choices
            allocated = False
            while (not allocated) and (not choice_list.end()):
                choice = choice_list.next()
                if AALst.num_alloc(choice) < DCapALst.capacity(choice):
                    AALst.add_stdnt(choice, element)
                    allocated = True
            if not allocated:
                raise RuntimeError
