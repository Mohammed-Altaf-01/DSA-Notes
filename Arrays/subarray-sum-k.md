Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

```python 
# Brute force O(N*N) solution 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0 
        n = len(nums)
        for i in range(n):
            _sum = 0 
            for j in range(i,n):
                _sum += nums[j]
                if _sum == k:
                    cnt += 1
        return cnt

```

```python 
# optimized using extra space 
# linear time with linear space

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      curSum = res = 0 
      prefixSum = {0 : 1}
      
      for n in nums:
        curSum += n 
        diff = curSum - k 
        res += prefixSum.get(diff,0)
        
        # adding the sum to map 
        prefixSum[curSum] = prefixSum.get(curSum,0) + 1
        
      return res
        

```