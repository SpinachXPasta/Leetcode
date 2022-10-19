#205. Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            
            if s[i] not in  s_to_t:
                s_to_t[s[i]] = []
            
            if t[i] not in t_to_s:
                t_to_s[t[i]] = []

            if t[i] not in s_to_t[s[i]]:
                s_to_t[s[i]].append(t[i])

            if s[i] not in t_to_s[t[i]]:
                t_to_s[t[i]].append(s[i])
            
            if len(t_to_s[t[i]]) > 1 or len(s_to_t[s[i]]) > 1:
                return False           
          
            if t_to_s[s_to_t[s[i]][0]][0] != s[i]:
                return False

            

          
        return True
