In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 
* one edge case to handle is when the nobody trusts anyone but there is only one person, then he is the judge
* But if there are more than one people exist and no one trust each other then no answer return -1 

```python 

from collections import defaultdict

class Node:
    def __init__(self):
        self.in_degree = 0 
        self.out_degree = 0 

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust == [] and n == 1:
            return 1
         
        degrees = defaultdict(Node)
        for u,v in trust:
            # out degree incremented for u 
            u_node = degrees[u]
            u_node.out_degree += 1

            # in degree incremented for v 
            v_node = degrees[v]
            v_node.in_degree += 1 
        
        for key, node in degrees.items():
            if node.out_degree == 0 and node.in_degree == (n-1):
                return key 
        
        return -1


        

```