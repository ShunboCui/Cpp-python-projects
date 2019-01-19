import CalcModule
def comparelist(list1, list2, name):
    if list1 == list2:
        print("Test passed, lists are equal for %s" % (name))
    else:
        print("Test failed, lists are not equal for %s" % (name))

def comparefloat(x, y, name):
    temp = x - y;
    if abs(temp) < 0.001:
        print("Test passed, floats are equal for %s" % (name))
    else:
        print("Test failed, floats are not equal for %s" % (name))

def comparedirectory(dir1, dir2, name):
    if dir1 == dir2:
        print("Test passed, directories are equal for %s" % (name))
    else:
        print("Test failed, directories are not equal for %s" % (name))

def sorttest1():
    emptylist = []
    sortedemptylist = CalcModule.sort(emptylist)
    comparelist(sortedemptylist, emptylist, 'sorting empty list')

def sorttest2():
    unsortedlist = [{'macid': 'A', 'gender': 'male', 'gpa': 7.4}, 
                    {'macid': 'B', 'gender': 'female', 'gpa': 3.7}, 
                    {'macid': 'C', 'gender': 'female', 'gpa': 8.2}, 
                    {'macid': 'D', 'gender': 'male', 'gpa': 6.7}, 
                    {'macid': 'E', 'gender': 'male', 'gpa': 9.1}]
    sortedlist = CalcModule.sort(unsortedlist)
    expected = [{'macid': 'E', 'gender': 'male', 'gpa': 9.1}, 
                {'macid': 'C', 'gender': 'female', 'gpa': 8.2}, 
                {'macid': 'A', 'gender': 'male', 'gpa': 7.4}, 
                {'macid': 'D', 'gender': 'male', 'gpa': 6.7}, 
                {'macid': 'B', 'gender': 'female', 'gpa': 3.7}]
    comparelist(sortedlist, expected, 'sorting added empty list')

def averagetest1():
    studentlist = [{'macid': 'A', 'gender': 'male', 'gpa': 7.4}, 
                    {'macid': 'B', 'gender': 'female', 'gpa': 3.7}, 
                    {'macid': 'C', 'gender': 'female', 'gpa': 8.2}, 
                    {'macid': 'D', 'gender': 'male', 'gpa': 6.7}, 
                    {'macid': 'E', 'gender': 'male', 'gpa': 9.1}]
    averageresult = CalcModule.average(studentlist, 'male')
    expected = 7.733
    comparefloat(expected, averageresult, 'calculating average gpa for male')

def averagetest2():
    studentlist = [{'macid': 'A', 'gender': 'male', 'gpa': 7.4}, 
                    {'macid': 'B', 'gender': 'female', 'gpa': 3.7}, 
                    {'macid': 'C', 'gender': 'female', 'gpa': 8.2}, 
                    {'macid': 'D', 'gender': 'male', 'gpa': 6.7}, 
                    {'macid': 'E', 'gender': 'male', 'gpa': 9.1}]
    averageresult = CalcModule.average(studentlist, 'female')
    expected = 5.95
    comparefloat(expected, averageresult, 'calculating average gpa for female')

def averagetest3():
    studentlist = []
    averageresult = CalcModule.average(studentlist, 'female')
    expected = 0
    comparefloat(expected, averageresult, 'calculating average gpa for empty list')

def allocatetest1():
    studentlist = [{'macid': 'A', 'gender': 'male', 'gpa': 7.4, 'choices': ['electrical', 'software', 'chemical']}, 
                    {'macid': 'B', 'gender': 'female', 'gpa': 3.7, 'choices': ['civil', 'materials', 'chemical']}, 
                    {'macid': 'C', 'gender': 'female', 'gpa': 8.2, 'choices': ['engphys', 'materials', 'electrical']}, 
                    {'macid': 'D', 'gender': 'male', 'gpa': 6.7, 'choices': ['software', 'civil', 'mechanical']}, 
                    {'macid': 'E', 'gender': 'male', 'gpa': 9.1, 'choices': ['chemical', 'materials', 'engphys']}]
    freelist = []
    capacity = {'civil': 5,
                'chemical': 5,
                'electrical': 5,
                'mechanical': 5,
                'software': 5,
                'materials': 5,
                'engphys': 5}
    expected = {'civil': [],
                'chemical': [{'macid': 'E', 'gender': 'male', 'gpa': 9.1, 'choices': ['chemical', 'materials', 'engphys']}],
                'electrical': [{'macid': 'A', 'gender': 'male', 'gpa': 7.4, 'choices': ['electrical', 'software', 'chemical']}],
                'mechanical': [],
                'software': [{'macid': 'D', 'gender': 'male', 'gpa': 6.7, 'choices': ['software', 'civil', 'mechanical']}],
                'materials': [],
                'engphys': [{'macid': 'C', 'gender': 'female', 'gpa': 8.2, 'choices': ['engphys', 'materials', 'electrical']}]}
    allocated = CalcModule.allocate(studentlist, freelist, capacity)
    comparedirectory(allocated, expected, 'allocating')

def allocatetest2():
    studentlist = []
    freelist = []
    capacity = {'civil': 5,
                'chemical': 5,
                'electrical': 5,
                'mechanical': 5,
                'software': 5,
                'materials': 5,
                'engphys': 5}
    expected = {'civil': [],
                'chemical': [],
                'electrical': [],
                'mechanical': [],
                'software': [],
                'materials': [],
                'engphys': []}
    allocated = CalcModule.allocate(studentlist, freelist, capacity)
    comparedirectory(allocated, expected, 'allocating empty list')

def allocatetest3():
    Studentlist = [{'macid': 'A', 'gender': 'male', 'gpa': 7.4, 'choices': ['civil', 'software', 'chemical']}, 
                    {'macid': 'B', 'gender': 'female', 'gpa': 7.3, 'choices': ['civil', 'materials', 'chemical']}, 
                    {'macid': 'C', 'gender': 'female', 'gpa': 8.2, 'choices': ['civil', 'materials', 'electrical']}, 
                    {'macid': 'D', 'gender': 'male', 'gpa': 6.7, 'choices': ['civil', 'software', 'mechanical']}, 
                    {'macid': 'E', 'gender': 'male', 'gpa': 9.1, 'choices': ['civil', 'materials', 'engphys']},
                    {'macid': 'F', 'gender': 'female', 'gpa': 10.1, 'choices': ['civil', 'mechanical', 'materials']}]
    Freelist = ['A', 'B', 'C', 'D', 'E', 'F']
    Capacity = {'civil': 5,
                'chemical': 5,
                'electrical': 5,
                'mechanical': 5,
                'software': 5,
                'materials': 5,
                'engphys': 5}
    expected = {'civil': [{'macid': 'A', 'gender': 'male', 'gpa': 7.4, 'choices': ['civil', 'software', 'chemical']}, 
                    {'macid': 'B', 'gender': 'female', 'gpa': 7.3, 'choices': ['civil', 'materials', 'chemical']}, 
                    {'macid': 'C', 'gender': 'female', 'gpa': 8.2, 'choices': ['civil', 'materials', 'electrical']}, 
                    {'macid': 'D', 'gender': 'male', 'gpa': 6.7, 'choices': ['civil', 'software', 'mechanical']}, 
                    {'macid': 'E', 'gender': 'male', 'gpa': 9.1, 'choices': ['civil', 'materials', 'engphys']},
                    ],
                'chemical': [],
                'electrical': [],
                'mechanical': [],
                'software': [],
                'materials': [],
                'engphys': []}
    allocated = CalcModule.allocate(Studentlist, Freelist, Capacity)
    comparedirectory(allocated, expected, 'allocating (all freechoice)')

def allocatetest4():
    Studentlist = [{'macid': 'A', 'gender': 'male', 'gpa': 7.4, 'choices': ['civil', 'software', 'chemical']}, 
                    {'macid': 'B', 'gender': 'female', 'gpa': 7.3, 'choices': ['civil', 'materials', 'chemical']}, 
                    {'macid': 'C', 'gender': 'female', 'gpa': 8.2, 'choices': ['civil', 'materials', 'electrical']}, 
                    {'macid': 'D', 'gender': 'male', 'gpa': 6.7, 'choices': ['civil', 'software', 'mechanical']}, 
                    {'macid': 'E', 'gender': 'male', 'gpa': 9.1, 'choices': ['civil', 'materials', 'engphys']},
                    {'macid': 'F', 'gender': 'female', 'gpa': 10.1, 'choices': ['civil', 'mechanical', 'materials']}]
    Freelist = ['A', 'B', 'C']
    Capacity = {'civil': 3,
                'chemical': 5,
                'electrical': 5,
                'mechanical': 5,
                'software': 5,
                'materials': 5,
                'engphys': 5}
    expected = {'civil': [{'macid': 'A', 'gender': 'male', 'gpa': 7.4, 'choices': ['civil', 'software', 'chemical']}, 
                    {'macid': 'B', 'gender': 'female', 'gpa': 7.3, 'choices': ['civil', 'materials', 'chemical']}, 
                    {'macid': 'C', 'gender': 'female', 'gpa': 8.2, 'choices': ['civil', 'materials', 'electrical']}],
                'chemical': [],
                'electrical': [],
                'mechanical': [{'macid': 'F', 'gender': 'female', 'gpa': 10.1, 'choices': ['civil', 'mechanical', 'materials']}],
                'software': [{'macid': 'D', 'gender': 'male', 'gpa': 6.7, 'choices': ['civil', 'software', 'mechanical']}],
                'materials': [{'macid': 'E', 'gender': 'male', 'gpa': 9.1, 'choices': ['civil', 'materials', 'engphys']}],
                'engphys': []}
    allocated = CalcModule.allocate(Studentlist, Freelist, Capacity)

    comparedirectory(allocated, expected, 'allocating (first choice full)')

def allocatetest5():
    Studentlist = [{'macid': 'A', 'gender': 'male', 'gpa': 7.4, 'choices': ['civil', 'software', 'chemical']}, 
                    {'macid': 'B', 'gender': 'female', 'gpa': 7.3, 'choices': ['civil', 'materials', 'chemical']}, 
                    {'macid': 'C', 'gender': 'female', 'gpa': 8.2, 'choices': ['civil', 'materials', 'electrical']}, 
                    {'macid': 'D', 'gender': 'male', 'gpa': 6.7, 'choices': ['civil', 'software', 'mechanical']}, 
                    {'macid': 'E', 'gender': 'male', 'gpa': 9.1, 'choices': ['civil', 'materials', 'engphys']},
                    {'macid': 'F', 'gender': 'female', 'gpa': 10.1, 'choices': ['civil', 'mechanical', 'materials']}]
    Freelist = ['A', 'B', 'C']
    Capacity = {'civil': 3,
                'chemical': 0,
                'electrical': 0,
                'mechanical': 0,
                'software': 0,
                'materials': 0,
                'engphys': 0}
    expected = {'civil': [{'macid': 'A', 'gender': 'male', 'gpa': 7.4, 'choices': ['civil', 'software', 'chemical']}, 
                    {'macid': 'B', 'gender': 'female', 'gpa': 7.3, 'choices': ['civil', 'materials', 'chemical']}, 
                    {'macid': 'C', 'gender': 'female', 'gpa': 8.2, 'choices': ['civil', 'materials', 'electrical']}],
                'chemical': [],
                'electrical': [],
                'mechanical': [],
                'software': [],
                'materials': [],
                'engphys': []}
    allocated = CalcModule.allocate(Studentlist, Freelist, Capacity)

    comparedirectory(allocated, expected, 'allocating (capacities full)')

sorttest1()
sorttest2()
averagetest1()
averagetest2()
averagetest3()
allocatetest1()
allocatetest2()
allocatetest3()
allocatetest4()
allocatetest5()