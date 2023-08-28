from collections import deque
def is_balanced(expression):
    # hold = []
    
    # for char in expression:
    #     if char in ["(","{","["]:
    #         hold.append(char)
    #     else:
    #         if not hold:
    #             return False
    #         current_char = hold.pop()
    #         if current_char == '(':
    #             if char != ')':
    #                 print(False)
    #                 return False 
    #             if current_char == '{':
    #                 if char != "}":
    #                     return False
    #             if current_char == '[':
    #                 if char != "]":
    #                     return False
    # if hold:
    #     print(False)
    #     return False
    # print(True)
    # return True      
    
    stack = deque()
    opening_brackets = '({['
    closing_brackets = ')}]'
    bracket_pairs = {')':'(', '}':'{', ']':'['}
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if stack[-1] == bracket_pairs[char]:
                stack.pop()
    return not stack                
                         
    
print(is_balanced("([]") )  

