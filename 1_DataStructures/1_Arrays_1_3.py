# 1.3 Calculate maximum subarray sum
'''
Given an array of numbers,find the maximum sum of any contiguous subarray of the array.
For example ,given the array [34,-50,42,14,-5,86],the maximum sum would be 137,
since we would take elements 42,14,-5,and 86.
Given the array [-5,-1,-8,-9],the maximum sum would be 0,since we would choose not to take any elements.

'''
# My solution
'''
a=[34,-50,42,14,-5,86]
actual=0
anterior=0
for i in range(len(a)):
    anterior=actual
    actual+=a[i]
    #print(str(i)+"x")
    if(actual<anterior):
        print(anterior)
        
print(actual)

print("")
actual1=0
anterior1=0
for i in range(len(a)-1,-1,-1):
    anterior1=actual1
    actual1+=a[i]
    #print(str(i)+"x")
    if(actual1<anterior1):
        print(anterior1)
        
print(actual1)
#Just insted of the print statement,you have to append inside a list and find the max value of the array
'''
