class Solution:
    def isPalindrome(self, s: str) -> bool:

        def is_alfanum(char):
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
                return True
            return False

        candidate = ""
        s = s.lower()
        for char in s:
            if is_alfanum(char):
                candidate += char

        if candidate == candidate[::-1]:
            return True
        return False
