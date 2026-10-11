class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        f = {}
        for ch in t:
            f[ch] = f.get(ch, 0) + 1

        return d == f