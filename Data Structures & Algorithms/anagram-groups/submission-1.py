class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s: str, t:str) -> bool:
            dict_s = {}
            dict_t = {}

            len_s = len(s)
            len_t = len(t)

            if len_s != len_t:
                return False
            
            for char_s in s:
                if char_s in dict_s:
                    dict_s[char_s] += 1
                else:
                    dict_s[char_s] = 1

            for char_t in t:
                if char_t in dict_t:
                    dict_t[char_t] += 1
                else:
                    dict_t[char_t] = 1
            
            if dict_t == dict_s:
                return True
            return False
        
        n = len(strs)
        output = []
        idx_used = set()
        group = []

        for i, str1 in enumerate(strs):
            if i not in idx_used:
                group.append(str1)
            
                for j in range(i+1, n):
                    str2 = strs[j]
                    if is_anagram(str1, str2):
                        group.append(str2)
                        idx_used.add(j)
                if group:
                    output.append(group)
                group = []

        return output
        
