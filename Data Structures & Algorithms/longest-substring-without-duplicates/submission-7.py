class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # se string vazia retorna 0
        # se string for 1 retona 1

        # 1. defino um set vazio e left e right pointers = 0 
        # 2. se o caracter atual estiver no set -> while loop diminuindo a janela até a janela nao conter duplicatas
        # 3. se não incremento right e adiciono o atual no set
        # 4. pego maior entre longest e r - l + 1

        l = 0
        longest = 0
        seen = set()
        n = len(s)
        for r in range(n):
            curr_char = s[r]
            if curr_char in seen:
                while curr_char in seen:
                    seen.remove(s[l])
                    l += 1
            
            seen.add(curr_char)
            longest = max(longest, r - l + 1)
        
        return longest


        


