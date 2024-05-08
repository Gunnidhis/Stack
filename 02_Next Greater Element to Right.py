
# @author
# Gunnidhi Sharma

# Problem: Given an array, find an array of Next Greater Elements (NGE) for every element.
# 		 The Next Greater Element for an element x is the first greater element
# 		 on the right side of x in array. Elements for which no greater element exist,
# 		 consider next greater element as -1.


# Intuition : In NGER, we will traverse from the right to the left to maintain the right greater element for each element.

#              In stack, we will contain the all the greater right elements for a perticular element to its right.
#                          01. if curr element is small than stack.top(),we will pop the element from stack until we get the element which is greater than curr.
#                          02. if stack.top() element is greater then curr element (i.e. since stack contain right greater element for each element hence this element will be in our answer array) 
def solve(arr):
    n=len(arr)
    stack = list()
    temp_arr = list()
    for i in range(n-1,-1,-1):
        curr = arr[i]
        
        while len(stack) != 0 and stack[-1] <= curr:
            stack.pop()
            
        if len(stack) == 0:
            temp_arr.append(-1)
            
        else:
            temp_arr.append(stack[-1])
            
        stack.append(curr)
        
    temp_arr.reverse()
    
    return temp_arr
    
        
        
    
if __name__ == "__main__":
    arr = [10, 7, 5, 4, 9, 2, 1]
    ans = solve(arr)
    print(ans)

#output [-1, 9, 9, 9, -1, -1, -1]
