# 1.1 Get product of all other elements
'''
Given an array of integers,return a new array such that each element at index i of the new array is
the product of all the numbers in the original array except the one at i.

For example,if our input was [1,2,3,4,5],the expected output would be [120,60,40,30,24].
If our input was [3,2,1],the expected output would be [2,3,6].

Follow-up:What if you can´t use division?


'''
# 0(n**2)
'''
a=[1,2,3,4,5]
def result(a):
    b={}
    for i in range(len(a)):
        b[i]=1
        for j in range(len(a)):
            if(i!=j):
                b[i]*=a[j]
                
    c=[b[x] for x in b] 
            
    return c
    
print(result(a))
'''
