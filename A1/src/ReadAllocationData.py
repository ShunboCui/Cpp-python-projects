## @file ReadAllocationData.py
#  @author 
#  @brief 
#  @date 

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