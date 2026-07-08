def calculate_dimensions(path):

    points = []

    for segment in path:
        points.append(segment.start)
        points.append(segment.end)


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