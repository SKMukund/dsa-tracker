class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        result = ""

        for c in num:
            while stack and k > 0 and c < stack[-1]:
                stack.pop() 
                k -= 1
            stack.append(c)
        
        if k > 0:
            stack = stack[:-k]
        
        result = "".join(stack).lstrip("0")

        return result if result else "0"
        