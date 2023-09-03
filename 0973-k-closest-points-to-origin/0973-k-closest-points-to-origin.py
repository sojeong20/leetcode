class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances_map = {}
        distances_lst = []
        for i, p in enumerate(points):
            distance = p[0]*p[0] + p[1]*p[1]
            distances_map[i] = distance
            distances_lst.append(distance)

        distances_lst = sorted(distances_lst)[:k]        
        point_indexes = [k for k, v in distances_map.items() if v in distances_lst] 

        return [points[i] for i in point_indexes]
    