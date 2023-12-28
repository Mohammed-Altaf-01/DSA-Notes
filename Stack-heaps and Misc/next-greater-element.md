The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

* There exist solution in multiple way using , Stacks, heap and looping one. But, using a mapping is compulsory. 

```python 
    # TC - O(N*M) SC-O(N)
    def iterative_soln(nums1,nums2):
        n2 = len(nums2)

        # storing the corresponding index for all values in number 2 
        idx_map = {}
        for i,num in enumerate(nums2):
            idx_map[num] = i 
        
        # getting the index for ith element in nums1 and moving further from that.
        for i,num in enumerate(nums1):
            idx = idx_map[num]
            changed = False
            for j in range(idx,n2):
                if nums2[j] > num:
                    nums1[i] = nums2[j]
                    changed = True 
                    break
            if not changed:
                nums1[i] = -1 
        
        return nums1
        # the above solution is inplace 
```

```python 
    # using stack which gives TC - O(N) AND SC - O(N)
    def stack(nums1,nums2):
        nxt_greater_map = {}
        stack = [nums2[0]]

        # making a kind of parent child relation based on top ele in stack.
        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                ele = stack.pop()
                nxt_greater_map[ele] = nums2[i]
            stack.append(nums2[i])
        
        return [nxt_greater_map.get(ele,-1) for ele in nums1]

```

```python 
    import heapq as H 

    def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        # starting from last elemnt adding each elements corresponding parent - child type 
        heap = []
        mapping = {}
        for i in range(len(nums2)-1,-1,-1):
            x = nums2[i]
            while heap and heap[0] <= x:
                H.heappop(heap)
    
            if heap:
                mapping[x] = heap[0]

            H.heappush(heap,x)
        
        return [mapping.get(ele,-1) for ele in nums1]

```

* I thought only the next immediate elemnt is to be found, but i was wrong we have to iterate the remaining array from that particular element. 
* understanding question clealy should be our first priority. 