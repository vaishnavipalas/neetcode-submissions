class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs:
                if stack:
                    check = stack.pop()
                    if pairs[char] != check:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True

        
        