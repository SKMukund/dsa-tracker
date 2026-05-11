class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        curr_num = 0
        curr_str = ""

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            
            elif c == "[":
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = ""
                curr_num = 0

            elif c == "]":
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + curr_str * num
            
            else:
                curr_str += c
            
        return curr_str

        