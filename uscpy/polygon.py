"""
A place for polygon functions.
"""

def area(vertices):
    """
    Calculate and return the area of a non-self intersecting polygon shape.

    Args:
        vertices: a list of 2d point tuples sorted by neighbor along perimeter

    This will return a negative value if the points are numbered in a clockwise
    order, but can still be used for correctly computing centroid coordinates.

    References:
     [1] http://en.wikipedia.org/wiki/Centroid#Centroid_of_polygon
     [2] http://paulbourke.net/geometry/polygonmesh/centroid.pdf
    """
    n = len(vertices)
    # if no vertex, area is undefined
    if n == 0:
        return None
    # no area with lines and points
    if n < 3:
        return 0
    accumulator = 0.0
    for i in xrange(n):
        x_i, y_i = vertices[i]
        x_i1, y_i1 = vertices[(i + 1) % n]
        accumulator += x_i * y_i1 - x_i1 * y_i
    return accumulator * 0.5

def centroid(vertices):
    """
    Calculate and return the centroid of a non-self intersecting polygon shape.

    Args:
        vertices: a list of 2d point tuples sorted by neighbor along perimeter

    References:
     [1] http://en.wikipedia.org/wiki/Centroid#Centroid_of_polygon
     [2] http://paulbourke.net/geometry/polygonmesh/centroid.pdf
    """
    n = len(vertices)
    # if no vertices, centroid is None
    if n == 0:
        return None
    poly_area = area(vertices)
    # if no area, centroid is first vertex
    if poly_area == 0:
        return vertices[0]
    accumulator_x = 0.0
    accumulator_y = 0.0
    for i in xrange(n):
        x_i, y_i = vertices[i]
        x_i1, y_i1 = vertices[(i + 1) % n]
        c = x_i * y_i1 - x_i1 * y_i
        accumulator_x += (x_i + x_i1) * c
        accumulator_y += (y_i + y_i1) * c
    scale = 1.0 / (6.0 * poly_area)
    return (accumulator_x * scale, accumulator_y * scale)
