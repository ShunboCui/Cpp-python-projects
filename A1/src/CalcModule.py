## @file CalcModule.py
#  @author 
#  @brief 
#  @date 

def sort(S):
    def gpa(s):
           return s['gpa'] 
    sortedlist = sorted(S,key = gpa)
    return (sortedlist)

def average(L, g):
    genderlist = []
    sum = 0
    count = 0
    for result in L:
        if result['gender'] == g:
            sum += result['gpa']
            count += 1
    return average

def allocate(S, F, C):
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

    materiallist = []
    materialcount = 0

    engphyslist = []
    engphyscount = 0

    freelist = []

    for allstudent in S:
        if allstudent['macid'] in F:
            S.remove(allstudent)
        if allstudent['macid'] in F and allstudent['gpa'] > 4:
            freelist.append(allstudent)

    for freestudent in freelist:
        if freestudent['choices'][0] == 'civil':
            civillist.append(freestudent)
            civilcount += 1
        elif freestudent['choices'][0] == 'chemical':
            chemicallist.append(freestudent)
            chemicalcount +=1
        elif freestudent['choices'][0] == 'electrical':
            electricallist.append(freestudent)
            electricalcount += 1
        elif freestudent['choices'][0] == 'mechanical':
            mechanicallist.append(freestudent)
            mechanicalcount += 1
        elif freestudent['choices'][0] == 'software':
            softwarelist.append(freestudent)
            softwarecount += 1
        elif freestudent['choices'][0] == 'material':
            materiallist.append(freestudent)
            materialcount += 1
        elif freestudent['choices'][0] == 'engphys':
            engphyslist.append(freestudent)
            engphyscount += 1

    sort(S)

    for unfreestudent in S:
        if unfreestudent['gpa'] > 4:
            if unfreestudent['choices'][0] == 'civil':
                civillist.append(unfreestudent)
                civilcount += 1
            elif unfreestudent['choices'][0] == 'chemical':
                chemicallist.append(unfreestudent)
                chemicalcount +=1
            elif unfreestudent['choices'][0] == 'electrical':
                electricallist.append(unfreestudent)
                electricalcount += 1
            elif unfreestudent['choices'][0] == 'mechanical':
                mechanicallist.append(unfreestudent)
                mechanicalcount += 1
            elif unfreestudent['choices'][0] == 'software':
                softwarelist.append(unfreestudent)
                softwarecount += 1
            elif unfreestudent['choices'][0] == 'material':
                materiallist.append(unfreestudent)
                materialcount += 1
            elif unfreestudent['choices'][0] == 'engphys':
                engphyslist.append(unfreestudent)
                engphyscount += 1

    allocated = {}
    allocated['civil'] = civillist
    allocated['chemical'] = chemicallist
    allocated['electrical'] = electricallist
    allocated['mechanical'] = mechanicallist
    allocated['software'] = softwarelist
    allocated['material'] = materiallist
    allocated['engphys'] = engphyslist
    return allocated
