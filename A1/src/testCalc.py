## @file testCalc.py
#  @author 
#  @brief 
#  @date 

import ReadAllocationData
import CalcModule
stdntslist = ReadAllocationData.readStdnts('1.txt')
freelist = ReadAllocationData.readFreeChoice('3.txt')
capacity = ReadAllocationData.readDeptCapacity('2.txt')
allocated = CalcModule.allocate(stdntslist, freelist, capacity)
print(allocated)