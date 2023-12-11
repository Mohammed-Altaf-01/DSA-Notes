"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 
"""

# this question can be solved using DutchNationalFlag Algorithm.
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(x,y):
            nums[x],nums[y] = nums[y],nums[x]
        
        low = mid = 0 
        high = len(nums)-1 

        while mid <= high:
            if nums[mid] == 1:
                mid += 1 
            elif nums[mid] == 0:
                swap(low,mid)
                low += 1
                mid += 1 
            else:
                swap(high,mid)
                high -= 1 
        
''' 
When nums[mid] is 2, it means we've found a 2. We swap the element at high with the element at mid (which is 2), and then decrement high. This ensures that 2s are moved to the right section.
The reason we don't increment mid when we swap with high is that after swapping, the element at mid is now an unknown value (it could be 0, 1, or 2). We need to re-evaluate it before deciding whether to move mid further or not. That's why we don't increment mid in the case of swapping with high.
'''           
        