Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

```python 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # calculate prefix 
        prefix = [1]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i]

        # calculate suffix 
        suffix = [1]*n
        suffix[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i]

        # put it in the result 
        res = [1]*n
        for j in range(n):
            # if we are at the first index 
            if j == 0:
                res[j] = suffix[j+1]
            # if we are at the last index 
            elif j == n-1:
                res[j] = prefix[j-1]
            # all the other indices
            else:
                res[j] = prefix[j-1] * suffix[j+1]
        
        return res

        

```