# @author
# Gunnidhi Sharma

# In this particular code, we'll be using inbuilt Stack Class because you are already familiar with
# the procedure that Stack works.

# Problem: Check whether the given string forms a set of Balanced Parenthesis or not.

# For example:

# Input: expression = "[[({})]]"
# Output: true

# Input: expression = "[[))"
# Output: false

# Input: expression = "[{]}"
# Output: false

# Intuition:

# 1. Whenever we encounter an openning bracket, we'll push it into the stack.
# 2. Whenever we encounter a closing bracket, we'll pop the element out of the stack and
#    we will check whether the popped element is same as the opening bracket of the category of
#    popped element.
# 3. If it satisfies for the complete process until the stack becomes empty, then the parenthesis
#    will be called as balanced, otherwise, if anywhere there is a mismatch, we'll directlty return false.



# this function will return true only when the popped element matches the category of the closing 
# bracket.
# Otherwise, we will return false.


# function which will return whether the expression is balanced or not */
def isBalanced(expression):
    stack = list()
    for each_bracket in expression:
        if (each_bracket == "(" or each_bracket == "{" or each_bracket == "["):
            stack.append(each_bracket)
        else:
            #first symbol is closed bracket then return False
            if ((len(stack) == 0 and each_bracket == "}") or (len(stack) == 0 and each_bracket == ")") or (len(stack) == 0 and  each_bracket == "]")):
                return False
            if (not isMatching(stack[-1],each_bracket)):
                return False
            
            stack.pop()
            
    if len(stack)==0:
        return 0
    
    return False
            
            
            
            
            
            
def isMatching(open_bracket,closed_bracket):
    if open_bracket=="(" and closed_bracket==")":
        return True
    if open_bracket=="{" and closed_bracket=="}":
        return True
    if open_bracket=="[" and closed_bracket=="]":
        return True
    return False

if __name__=="__main__":
    expression = "()[]{}"
    ans = isBalanced(expression)
    print(ans)
    
    
