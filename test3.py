def solution(S):

    stack = []

    for token in S.split():

        if token.isdigit():
            if int(token) >= 2**20:
                return -1  # integer is too large
            stack.append(int(token))
        
        elif token == "POP":
            not_stack(stack)
            stack.pop()
        
        elif token == "DUP":
            not_stack(stack)
            stack.append(stack[-1])
        
        elif token == "+":
            if len(stack) < 2:
                return -1  # error
            a = stack.pop()
            b = stack.pop()
            if a + b >= 2**20:
                return -1  # integer is too large
            stack.append(a + b)
        
        elif token == "-":
            if len(stack) < 2:
                return -1  # error
            a = stack.pop()
            b = stack.pop()
            if b > a:
                return -1  # subtraction is a negative result
            stack.append(a - b)
    
    not_stack(stack)
    
    return stack[-1] # default error value

def not_stack(stack):
    if not stack:
        return -1  # error
    pass

S = '4 5 6 - 7 +'
#S = '13 DUP 4 POP 5 DUP + DUP + -'
#S = '5 6 + -'
#S = '3 DUP 5 - -'
print(solution(S))