# 1.2 Locate smallest window to be sorted
'''
Given an array of integers that are out of order,determine the bounds of the smallest
window that must be sorted in order for the entire array to be sorted.

For example,given [3,7,5,6,9],you should return (1,3).

'''
#Solution 1
'''
def window(array):
    left,right=None,None
    s=sorted(array)
    
    for i in range(len(array)):
        if array[i] != s[i] and left is None:
            left=i
            #print(left)
            
        elif array[i] != s[i]:
            right=i
            #print(right)
            
    return left,right
    
print(window([3,7,5,6,9]))

'''
#Solution 2
'''
def window(array):
    left,right=None,None
    n=len(array)
    max_seen,min_seen=-float("inf"),float("inf")
    
    for i in range(n):
        max_seen=max(max_seen,array[i])
        #print(max_seen)
        if array[i] < max_seen:
            right=i
            #print(right)
            
    for i in range(n-1,-1,-1):
        min_seen=min(min_seen,array[i])
        #print(min_seen)
        if array[i] > min_seen:
            left=i
            #print(left)
        
            
    return left,right
    
print(window([3,7,5,6,9]))
'''
