import math


def get_test_points(contour):
    """
    Returns important points from a contour
    for containment testing.
    """

    points = []

    for segment in contour.path:

        points.append(
            (
                segment.start.real,
                segment.start.imag
            )
        )

    return points



def point_inside_circle(point, center, radius):
    """
    Checks if a point lies inside a circle.
    """

    x, y = point

    cx, cy = center

    distance = math.sqrt(
        (x - cx) ** 2 +
        (y - cy) ** 2
    )

    return distance <= radius



def point_inside_rectangle(point, xmin, xmax, ymin, ymax):
    """
    Checks if a point lies inside a rectangle.
    """

    x, y = point

    return (
        xmin <= x <= xmax
        and
        ymin <= y <= ymax
    )



def get_bounds(contour):
    """
    Calculates bounding box of contour.
    """

    points = get_test_points(contour)

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]


    return (
        min(xs),
        max(xs),
        min(ys),
        max(ys)
    )



def contour_contains(outer, inner):
    """
    Determines whether one contour contains another.

    Temporary implementation:
    Uses bounding boxes.

    Later:
    Replace with true geometric testing.
    """

    outer_xmin, outer_xmax, outer_ymin, outer_ymax = get_bounds(outer)

    inner_points = get_test_points(inner)


    for point in inner_points:

        if not point_inside_rectangle(
            point,
            outer_xmin,
            outer_xmax,
            outer_ymin,
            outer_ymax
        ):
            return False


    return True
