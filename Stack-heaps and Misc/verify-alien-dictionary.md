In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character


```python 
class Solution:
    def CheckOrder(self,words,order_map):
        def isSorted(a,b,idx):
            # if we have only one word
            if len(words) == 1:
                return True

            if idx >= len(a) or idx >= len(b):
                if len(a) == len(b) or len(a) < len(b):
                    return True 
                else:
                    return False

            if a[idx] == b[idx]:
                condition = isSorted(a,b,idx+1)
            else:
                a_ord = order_map[a[idx]]
                b_ord = order_map[b[idx]]
                condition = True if a_ord < b_ord else False 
            
            return condition
        
        # iterating over each word to check order 
        i = 0 
        for j in range(1,len(words)):
            check = isSorted(words[i],words[j],0)
            print(check)
            if not check:
                return False
            i += 1 
        return True 

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # creating mapping for each char in word to describe it's occurence
        order_map = {}
        for i,c in enumerate(order):
            order_map[c] = i

        # more than one word
        return self.CheckOrder(words,order_map) 

```


* I have wrote the recursive function wrong, have not stored the output and returned it each time 
* I should have thinked more creatively about the inputs, like the first word being small than second etc...