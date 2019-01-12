## @file ReadAllocationData.py
#  @author 
#  @brief 
#  @date 

f = open('1.txt', 'r')                  
n = 0
list1 = []
for line in f.readlines():
    v = line.strip().split(':')
    result = {}
    result['macid'] = v[0]
    result['fname'] = v[1]
    result['lname'] = v[2]
    result['gender'] = v[3]
    result['gpa'] = v[4]
    list1.append(result)
f.close()
for result in list1:
    print(result)