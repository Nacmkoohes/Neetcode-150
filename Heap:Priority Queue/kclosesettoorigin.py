# class Solution:
#     def kClosest(self, points: list[List[int]], k: int) -> List[List[int]]:
#         for point in points:
#             point.append(point[0]**2 + point[1]**2)
#             # Sort by the distance from the origin
#         points.sort(key=lambda x: x[2])
#         return [[point[0],point[1]] for point in points[:k]]
import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def distance(point):
            return point[0]**2 + point[1]**2
        
        heap = []
        for x, y in points:
            dist = distance([x, y])
            if len(heap) < k:
                heapq.heappush(heap, (-dist, [x, y]))
#- dist is negated to create a max-heap cause heapq is a min-heap by default
            else:
                heapq.heappushpop(heap, (-dist, [x, y]))
        return [[x,y] for dist, (x, y) in heap]
