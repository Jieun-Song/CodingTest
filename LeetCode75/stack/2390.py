class Solution:
    def removeStars(self, s: str) -> str:
        stack1, stack2 = list(), list(s)
        stack2.reverse()
        len2 = len(stack2)
        while len(stack2) != 0:
            popped = stack2.pop()
            if popped == "*" and len(stack1) != 0:
                stack1.pop()
            else:
                stack1.append(popped)
            
        return "".join(stack1)