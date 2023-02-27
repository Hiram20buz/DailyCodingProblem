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
# Solution
b=[1,2,3,4,5]

def products(nums):
    prefix_products=[]
    
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1]*num)
            
        else:
            prefix_products.append(num)
            
    #print(prefix_products)
    
    suffix_products=[]
    
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1]*num)
            
        else:
            suffix_products.append(num)
            
    suffix_products=list(reversed(suffix_products))
    #print(suffix_products)
    
    result=[]
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i==len(nums)-1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1]*suffix_products[i+1])
            
    #print(result)
    return result
        

        

    
print(products(b))
