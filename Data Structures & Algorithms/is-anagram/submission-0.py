class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        f={}
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in d:
                    d[i] +=1
                else:
                    d[i]=1
            for j in t:
                if j in f:
                    f[j] +=1
                else:
                    f[j]=1
        if d==f:
            return True
        else:
            return False