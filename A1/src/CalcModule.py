## @file CalcModule.py
#  @title CalcModule
#  @author Shunbo Cui
#  @date 1/18/2019

## @brief This function sorts the list of students according to their gpa.
#  @param S List of students
#  @return Return the sorted list of students
def sort(S):
    def gpa(s):
           return s['gpa'] 
    sortedlist = sorted(S,key = gpa,reverse = True)
    return (sortedlist)

## @brief This function calculates the average gpa in a list according to the gender.
#  @param L List of students
#  @param g The determined gender
#  @return Return the average gpa
def average(L, g):
    genderlist = []
    sum = 0
    count = 0
    if L == []:
        return 0
    for result in L:
        if result['gender'] == g:
            sum += result['gpa']
            count += 1
    average = sum / count
    return average

## @brief This function allocated students to departments according to the gpa and the capacities.
#  @param S List of all students
#  @param F List of students with free choice
#  @return Return the allocated list
def allocate(S, F, C):
    #Creating empty lists for each department
    civillist = []
    civilcount = 0

    chemicallist = []
    chemicalcount = 0

    electricallist = []
    electricalcount = 0

    mechanicallist = []
    mechanicalcount = 0

    softwarelist = []
    softwarecount = 0

    materialslist = []
    materialscount = 0

    engphyslist = []
    engphyscount = 0

    #Createing a list for students with free choice
    freelist = []

    t = S.copy()
    for allstudent in t:
        if allstudent['macid'] in F:
             S.remove(allstudent)
             if allstudent['gpa'] > 4:
                freelist.append(allstudent)
           


    #Allocate the students with free choice according to their first choice
    for freestudent in freelist:
        if freestudent['choices'][0] == 'civil' and civilcount < C['civil']:
            civillist.append(freestudent)
            civilcount += 1
        elif freestudent['choices'][0] == 'chemical'and chemicalcount < C['chemical']:
            chemicallist.append(freestudent)
            chemicalcount +=1
        elif freestudent['choices'][0] == 'electrical'and electricalcount < C['electrical']:
            electricallist.append(freestudent)
            electricalcount += 1
        elif freestudent['choices'][0] == 'mechanical'and mechanicalcount < C['mechanical']:
            mechanicallist.append(freestudent)
            mechanicalcount += 1
        elif freestudent['choices'][0] == 'software'and softwarecount < C['software']:
            softwarelist.append(freestudent)
            softwarecount += 1
        elif freestudent['choices'][0] == 'materials'and materialscount < C['materials']:
            materialslist.append(freestudent)
            materialscount += 1
        elif freestudent['choices'][0] == 'engphys'and engphyscount < C['engphys']:
            engphyslist.append(freestudent)
            engphyscount += 1
        #If the capacity of any department is not enough for students with free choice
        else:
            print('Student %s with freechoice is not allocated bacause the first choice department is full' % (freestudent['macid']))

    sort(S)

    #Allocate the students without free choice according to their first choice when the department is not full
    for unfreestudent in S:
        if unfreestudent['gpa'] > 4.0:
            if unfreestudent['choices'][0] == 'civil'and civilcount < C['civil']:
                civillist.append(unfreestudent)
                civilcount += 1
            elif unfreestudent['choices'][0] == 'chemical'and chemicalcount < C['chemical']:
                chemicallist.append(unfreestudent)
                chemicalcount +=1
            elif unfreestudent['choices'][0] == 'electrical'and electricalcount < C['electrical']:
                electricallist.append(unfreestudent)
                electricalcount += 1
            elif unfreestudent['choices'][0] == 'mechanical'and mechanicalcount < C['mechanical']:
                mechanicallist.append(unfreestudent)
                mechanicalcount += 1
            elif unfreestudent['choices'][0] == 'software'and softwarecount < C['software']:
                softwarelist.append(unfreestudent)
                softwarecount += 1
            elif unfreestudent['choices'][0] == 'materials'and materialscount < C['materials']:
                materialslist.append(unfreestudent)
                materialscount += 1
            elif unfreestudent['choices'][0] == 'engphys'and engphyscount < C['engphys']:
                engphyslist.append(unfreestudent)
                engphyscount += 1
            #If the department is full, allocate them according to their second choice
            elif unfreestudent['choices'][1] == 'civil'and civilcount < C['civil']:
                civillist.append(unfreestudent)
                civilcount += 1
            elif unfreestudent['choices'][1] == 'chemical'and chemicalcount < C['chemical']:
                chemicallist.append(unfreestudent)
                chemicalcount +=1
            elif unfreestudent['choices'][1] == 'electrical'and electricalcount < C['electrical']:
                electricallist.append(unfreestudent)
                electricalcount += 1
            elif unfreestudent['choices'][1] == 'mechanical'and mechanicalcount < C['mechanical']:
                mechanicallist.append(unfreestudent)
                mechanicalcount += 1
            elif unfreestudent['choices'][1] == 'software'and softwarecount < C['software']:
                softwarelist.append(unfreestudent)
                softwarecount += 1
            elif unfreestudent['choices'][1] == 'materials'and materialscount < C['materials']:
                materialslist.append(unfreestudent)
                materialscount += 1
            elif unfreestudent['choices'][1] == 'engphys'and engphyscount < C['engphys']:
                engphyslist.append(unfreestudent)
                engphyscount += 1
            #If the department is full, allocate them according to their third choice
            elif unfreestudent['choices'][2] == 'civil'and civilcount < C['civil']:
                civillist.append(unfreestudent)
                civilcount += 1
            elif unfreestudent['choices'][2] == 'chemical'and chemicalcount < C['chemical']:
                chemicallist.append(unfreestudent)
                chemicalcount +=1
            elif unfreestudent['choices'][2] == 'electrical'and electricalcount < C['electrical']:
                electricallist.append(unfreestudent)
                electricalcount += 1
            elif unfreestudent['choices'][2] == 'mechanical'and mechanicalcount < C['mechanical']:
                mechanicallist.append(unfreestudent)
                mechanicalcount += 1
            elif unfreestudent['choices'][2] == 'software'and softwarecount < C['software']:
                softwarelist.append(unfreestudent)
                softwarecount += 1
            elif unfreestudent['choices'][2] == 'materials'and materialscount < C['materials']:
                materialslist.append(unfreestudent)
                materialscount += 1
            elif unfreestudent['choices'][2] == 'engphys'and engphyscount < C['engphys']:
                engphyslist.append(unfreestudent)
                engphyscount += 1
            #If the department of every department in the choice list is full
            else:
                print('Student %s  is not allocated bacause the departments are full' % (unfreestudent['macid']))

    allocated = {}
    allocated['civil'] = civillist
    allocated['chemical'] = chemicallist
    allocated['electrical'] = electricallist
    allocated['mechanical'] = mechanicallist
    allocated['software'] = softwarelist
    allocated['materials'] = materialslist
    allocated['engphys'] = engphyslist
    return allocated
