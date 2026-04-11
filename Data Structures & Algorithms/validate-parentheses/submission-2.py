class Solution:
    def isValid(self, s: str) -> bool:
        # verificar se esta fechando sem abrir

        stack = []
        close_to_open = {
            "}":"{",
            "]":"[",
            ")":"(" 
        }

        for char in s:
            if char in close_to_open:
                if not stack:
                    return False
                if stack[-1] != close_to_open[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        if not stack:
            return True
        return False

        