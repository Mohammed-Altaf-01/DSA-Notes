Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

```python 
import heapq as H 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # simple case but below not neccessary to add 
        if k == len(points):
            return points
        
        # finding the euclidian distance and adding to priority queue    
        euclid_dist = lambda x,y: int((x*x) + (y*y))
        heap = []
        for point in points:
            dist = euclid_dist(*point)
            H.heappush(heap,(dist,point))
        
        # return the kth smallest elements
        return [i[1] for i in H.nsmallest(k,heap)]


```