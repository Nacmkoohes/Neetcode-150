class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for t in tokens:
            #t operator:
            if t in "+-*/":
                x=stack.pop()
                y=stack.pop()
                if t=="+":
                    stack.append(x+y)
                if t=="-":
                    stack.append(y-x)
                if t=="*":
                    stack.append(x*y)
                if t=="/":
                    if x==0:
                        raise ZeroDivisionError("Cannot divide by zero")
                    stack.append(int(y/x))
            #t not operator
            else:
                stack.append(int(t))
        return stack[0]
        



