"""
Q4 The position of some particles on the horizontal x-axis are -12,
-4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the
positive direction. Extract these numbers from this whole text and
find the distance between the two furthest particles.
 points = [-1,2,-4,-3,-1,0,4,8]
 sorted_points = [-4, -3, -1, -1, 0, 2, 4, 8]
 distance = 8 -(-4) # 12
"""
import re
def distance(text):
    pattern = r'-?\d'
    match = re.findall(pattern, text)
    lst = [int(i) for i in match]
    lst.sort()
    return lst[-1] - lst[0]
text = """The position of some particles on the horizontal x-axis are -12,
            -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the
            positive direction"""
print('distance=',distance(text))
