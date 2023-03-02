# 3.1 Reversed linked list 
'''
Given the head of a singly linked list,reverse it in-place
'''
class Node(object):
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
        
b=Node(1)      
a=Node(12,b)

print(a.data) 

def reverse(head):
    prev,current=None,head
    while current is not None:
        tmp=current.next
        current.next=prev
        prev=current
        current=tmp
        
    return prev
    
print(reverse(a).data)
