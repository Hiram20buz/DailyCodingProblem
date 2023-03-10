# 2.1 Find the anagram indices
'''
Given a word w and a string s,find all indices in s which are the starting locations 
of anagrams of w.
For  example ,given w is ab and s is abxaba,return [0,3,4]
'''
# Python program to search all
# anagrams of a pattern in a text
  
MAX = 256 
  
# This function returns true
# if contents of arr1[] and arr2[]
# are same, otherwise false.
def compare(arr1, arr2):
    for i in range(MAX):
        if arr1[i] != arr2[i]:
            return False
    return True
      
# This function search for all
# permutations of pat[] in txt[]  
def search(pat, txt):
  
    M = len(pat)
    N = len(txt)
  
    # countP[]:  Store count of
    # all characters of pattern
    # countTW[]: Store count of
    # current window of text
    countP = [0]*MAX
  
    countTW = [0]*MAX
  
    for i in range(M):
        (countP[ord(pat[i]) ]) += 1
        (countTW[ord(txt[i]) ]) += 1
  
    # Traverse through remaining
    # characters of pattern
    for i in range(M, N):
  
        # Compare counts of current
        # window of text with
        # counts of pattern[]
        if compare(countP, countTW):
            print("Found at Index", (i-M))
  
        # Add current character to current window
        (countTW[ ord(txt[i]) ]) += 1
  
        # Remove the first character of previous window
        (countTW[ ord(txt[i-M]) ]) -= 1
      
    # Check for the last window in text    
    if compare(countP, countTW):
        print("Found at Index", N-M)
          
# Driver program to test above function       
txt = "abxaba"
pat = "ab"       
search(pat, txt)   
  
# This code is contributed
# by Upendra Singh Bartwal
