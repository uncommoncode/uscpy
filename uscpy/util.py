"""
Various utility functions live here.
"""

def point2ituple(point):
    """
    Returns an integer tuple for a floating point point.
    """
    return tuple([int(x) for x in point])
    

def flat_contour_iter(contour):
    """
    A generator for flat contours from a list of list of contours.
    """
    for chain in contour:
        yield chain[0]
