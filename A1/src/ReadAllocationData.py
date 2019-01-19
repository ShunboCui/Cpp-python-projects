## @file ReadAllocationData.py
#  @title ReadAllocationData
#  @author Shunbo Cui
#  @date 1/17/2019

## @brief This function reads detailed information of students.
#  @param s Name of list file
#  @return Return the list of students
def readStdnts(s):
    f = open('1.txt', 'r', -1, 'utf-8-sig')                  
    n = 0
    S = []
    for line in f.readlines():
        v = line.strip().split(':')
        result = {}
        choices = []
        result['macid'] = v[0]
        result['fname'] = v[1]
        result['lname'] = v[2]
        result['gender'] = v[3]
        result['gpa'] = float(v[4])
        choices.append(v[5])
        choices.append(v[6])
        choices.append(v[7])
        result['choices'] = choices
        S.append(result)
    f.close()
    return(S)

## @brief This function reads macid of students with freechoice.
#  @param s Name of list file
#  @return Return the list of students with free choice
def readFreeChoice(s):
    f = open(s, 'r', -1, 'utf-8-sig')                  

    F = []
    for line in f.readlines():
        v = line.strip()
        F.append(v)
    f.close()
    return (F)

## @brief This function reads capacity of each department from the file
#  @param s Name of list file
#  @return Return list of departments and their capacity
def readDeptCapacity(s):
    f = open(s, 'r', -1, 'utf-8-sig')     
    C = {}
    count = 0
    for line in f.readlines():
        v = line.strip().split(':')
        C[v[0]] = int(v[1])
    return (C)
