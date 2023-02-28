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
            left=1
            #print(left)
            
        elif array[i] != s[i]:
            right=i
            #print(right)
            
    return left,right
    
print(window([3,7,5,6,9]))



'''
