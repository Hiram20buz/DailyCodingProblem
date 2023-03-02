# 1.4 Find number of smaller elements to the rigth
'''
Given an array of integers,return a new array where each element in the new array
is the number of smaller elements to the rigth of that element in the original input array.

For example,given the array [3,4,9,6,1],return [1,1,2,1,0]
'''

import bisect

def smaller_counts(lst):
    result=[]
    seen=[]
    
    for num in reversed(lst):
        i=bisect.bisect_left(seen,num)
        #print(num)
        result.append(i)
        bisect.insort(seen,num)
        
    return list(reversed(result))
    
print(smaller_counts([3,4,9,6,1]))
