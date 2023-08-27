def is_balanced(expression):
    hold = []
    
    for char in expression:
        if char in ["(","{","["]:
            hold.append(char)
        else:
            if not hold:
                return False
            current_char = hold.pop()
            if current_char == '(':
                if char != ')':
                    print(False)
                    return False 
                if current_char == '{':
                    if char != "}":
                        return False
                if current_char == '[':
                    if char != "]":
                        return False
    if hold:
        print(False)
        return False
    print(True)
    return True                   
    
is_balanced("([]{})")    