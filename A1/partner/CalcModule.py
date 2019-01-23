## @file CalcModule.py
#  @author Dominik Buszowiecki
#  @brief Functions that can manipulate data given by the functions in ReadAllocataionData.py
#  @date 1/18/2019

from ReadAllocationData import *

## @brief Sorts students by there GPA (Descending).
#  @details The function is given a list of students. This list is created by the readStdnts(s) function in
#           ReadAllocationData.py. The function will sort the students
#           by there GPA, but in descending order and then return it. \n \n
#           REFERENCES: \n
#           Sorted function implementation: \n
#           https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
# @param S A list of dictionaries where each Dictionary represents a student.
# @return  The original list of students, but sorted by GPA.
def sort(S):
    newList = sorted(S, key=lambda gpa: float(gpa['gpa']), reverse=True)
    return newList


## @brief Calculates the average of either male or female students.
#  @details The function is given a list of students as well as a gender. Based on the gender given, the function
#           computes the average GPA of that gender in the list. If the gender is neither 'male' or 'female'
#           the function will provide an error message and return -1. If there are 0 students of a particular gender
#           and you compute the average of that gender, the function returns -1.
#  @param L A list of dictionaries. Each Dictionary represents a student.
#  @param g A string, must be either 'male' or 'female'.
#  @return Returns the average of the gender as a float.
def average(L,g):
    Flag = False
    if len(L) <= 0:
        return -1
    if g != 'male' and g!= 'female':
        print("ERROR: Gender should be 'male' or 'female' (Note: Case Sensitive)")
        return -1
    else:
        sum=0.0
        total=0
        for i in range(len(L)):
            if L[i]['gender'] == g:
                sum += L[i]['gpa']
                total += 1
                Flag = True
        if Flag == False:
            return -1
        return sum/total


## @brief Allocates students into a 2nd year Engineering program.
#  @details All students that have a GPA below 4.0, are not given a program. Students who were given free choice and
#           have a GPA above 4.0 are automatically assigned there first choice. The function does NOT check the program
#           capacity for free choice students. The rest of the students are given there choice based on there
#           GPA. If there first choice is full, they are given there second, if that is full, there third.
#           If all choices are full for a student, they are not given a program and a error is outputted.
#  @param S A list of dictionaries. Each Dictionary represents a student.
#  @param F A list of strings. Each string represents a macid of a student with Free choice.
#  @param C A dictionary. The dictionary contains the program and its capacity.
#  @return A dictionary that contains the programs and each student in that program.
def allocate (S, F, C):
    temp = sort(S).copy()
    tempC = C.copy()
    programs = {'civil': [], 'chemical': [], 'electrical': [], 'mechanical': [], 'software': [], 'materials': [], 'engphys': []}

    i=0
    while i < len(temp):
        if temp[i]['gpa'] < 4.0:
            del temp[i]
        elif temp[i]['macid'] in F:
            programs[temp[i]['choices'][0]].append(temp[i])
            if (tempC[temp[i]['choices'][0]]) <= 0:
                print("WARNING: Capacity below 0 for ", temp[i]['choices'][0])
            tempC[temp[i]['choices'][0]] -= 1
            del temp[i]
        else:
            i+=1

    while (len(temp) > 0):
        if tempC[temp[0]['choices'][0]] > 0:
            programs[temp[0]['choices'][0]].append(temp[0])
            tempC[temp[0]['choices'][0]] -= 1
            del temp[0]
        elif tempC[temp[0]['choices'][1]] > 0:
            programs[temp[0]['choices'][1]].append(temp[0])
            tempC[temp[0]['choices'][1]] -= 1
            del temp[0]
        elif tempC[temp[0]['choices'][2]] > 0:
            programs[temp[0]['choices'][2]].append(temp[0])
            tempC[temp[0]['choices'][2]] -= 1
            del temp[0]
        else:
            print("ERROR: Could not allocate macid:", temp[0]['macid'], ", all 3 program choices are full!")
            del temp[0]

    return programs