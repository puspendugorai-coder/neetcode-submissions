class Solution:
    def hasDuplicate(self, nums):
        l= []
        for i in nums:
            if i not in l:
                l.append(i)
            else:
                if i in l:
                    return True
        else:
            return False