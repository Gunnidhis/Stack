
# @author
# Gunnidhi Sharma

# Problem: Given an array, print the Next Greater Element (NGE) for every element.
# 		 The Next Greater Element for an element x is the first greater element
# 		 on the left side of x in array. Elements for which no greater element exist,
# 		 consider next greater element as -1.

def solve(arr):
    stack = list()
    temp_arr = list()

    n = len(arr)
    
    for i in range(n):
        curr = arr[i]
        while len(stack) != 0 and stack[-1] <= curr:
            stack.pop()
            
            
        if len(stack) == 0:
            temp_arr.append(-1)
            
        elif stack[-1]>=curr:
            temp_arr.append(stack[-1])
            
        stack.append(curr)
        
    return temp_arr
            
            
        
        

if __name__ == "__main__":
    arr = [4, 3, 9, 5, 6, 2, 7]
    ans = solve(arr)
    print(ans)

#output : [-1, 4, -1, 9, 9, 6, 9]
