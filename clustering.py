from turtle import Vec2D
from linear_algebra import Vector


def num_differences(v1: Vector, v2: Vector) -> int:
    assert len(v1) == len(v2)
    return len([x1 for x1,x2 in zip(v1,v2) if x1!=x2])

assert num_differences([1,2,3], [2,1,3]) == 2, 'number not equel to 2'
assert num_differences([1,2],[1,2]) == 0

def vector_equal(v1: Vector, v2:Vector) -> Vector:
    assert len(v1) == len(v2), 'the vectors not equal'
    return [x1 for x1,x2 in zip(v1,v2) if x1==x2]

assert vector_equal([1,2,3],[2,1,3]) == [3] , 'not equal'
assert vector_equal([1,2],[1,2]) == [1,2], 'not equal'