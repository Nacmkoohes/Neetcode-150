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
                    stack.append(x-y)
                if t=="*":
                    stack.append(x*y)
                if t=="/":
                    stack.append(int(x/y))
            return stack
        
tokens = ["1", "2", "+", "3", "*", "4", "-"]
print(Solution().evalRPN(tokens))


