class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     s_map = Counter(s)
        #     t_map = Counter(t)
        #     for num in s:
        #         if s_map[num] != t_map[num]:
        #             return False
        #     return True
        # else:
        #     return False
        return Counter(s) == Counter(t)
            
        