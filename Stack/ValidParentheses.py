class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
        #The char is opening
            if char  not in hashmap:
                stack.append(char)
            #The char is closing
            elif char in hashmap:
                if not stack:
                    return False
                else:
                    top_element=stack.pop()
                    if top_element != hashmap[char]:
                        return False
        #not stack because if stack empty True else False
        return not stack
                