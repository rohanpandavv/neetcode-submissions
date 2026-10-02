class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s, sorted_t = "".join(sorted(s)), "".join(sorted(t))
        if sorted_s == sorted_t:
            return True
        return False
        