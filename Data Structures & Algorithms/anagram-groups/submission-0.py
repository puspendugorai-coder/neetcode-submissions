from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]):
        l=[]
        d={}
        for i in strs:
            x= "".join(sorted(i))
            if x not in d:
                d.setdefault(x,[]).append(i)
            elif x in d:
                d[x].append(i)
        for j in d:
            l.append(d[j])
        return l


