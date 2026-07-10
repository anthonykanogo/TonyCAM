import math


def calculate_dimensions(path):

    points = []

    for segment in path:

        # Add start and end points
        points.append(segment.start)
        points.append(segment.end)


        # Arc support
        if hasattr(segment, "center"):

            center = segment.center

            radius = abs(segment.radius.real)


            # Add cardinal points of the circle
            # This captures the real bounds

            points.append(
                center + radius
            )

            points.append(
                center - radius
            )

            points.append(
                center + complex(0, radius)
            )

            points.append(
                center - complex(0, radius)
            )


    xs = []
    ys = []


    for point in points:

        xs.append(point.real)
        ys.append(point.imag)



    min_x = min(xs)
    max_x = max(xs)

    min_y = min(ys)
    max_y = max(ys)


    width = max_x - min_x
    height = max_y - min_y


    return width, height