##  @file DCapALst.py
#   @author Mengxi (William) Lei, leim5
#   @date Created 2019/02/05
#   @date Last modified 2019/02/09
#   @brief Class for the department capacity


##  @brief Holds a dictionary of the department capacity and manipulate it
class DCapALst:

    seq = None

    ##  @brief Construct the object, set the dictionary to a empty one
    @staticmethod
    def init():
        DCapALst.seq = {}

    ##  @brief Add the department capacity information to dictionary
    #   @param department department being added
    #   @param size capacity of the department
    #   @throws KeyError Department already in dictionary
    @staticmethod
    def add(department, size):
        if DCapALst.elm(department):
            raise KeyError
        else:
            DCapALst.seq[department] = size

    ##  @brief Delete the department capacity information from dictionary
    #   @param department department being deleted
    #   @throws KeyError Department not in dictionary
    @staticmethod
    def remove(department):
        if DCapALst.elm(department):
            del DCapALst.seq[department]
        else:
            raise KeyError

    ##  @brief Check if the element is inside the current dictionary
    #   @param department department being checked
    #   @return boolean state if the department is in the dictionary or not
    @staticmethod
    def elm(department):
        if department in DCapALst.seq:
            return True
        else:
            return False

    ##  @brief Check the capacity of the given department
    #   @param department department being checked
    #   @return the capacity of the department
    #   @throws KeyError the department is not in the dictionary
    @staticmethod
    def capacity(department):
        if DCapALst.elm(department):
            return DCapALst.seq[department]
        else:
            raise KeyError
