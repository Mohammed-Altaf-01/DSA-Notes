"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # find the last occurence of each character 
        last = {c:i for i, c in enumerate(s)}
        j = anchor = 0 
        res = []
        for i, c in enumerate(s):
            j = max(j,last[c])
            if i == j: # if we have reached last occurence of a char then it's the partition point
                res.append(i-anchor+1)
                anchor = i + 1 
        return res 