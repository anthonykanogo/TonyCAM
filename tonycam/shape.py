def classify_shape(path):

    segments = len(path)

    # Check for circles
    if segments == 2:

        arc_count = 0

        for segment in path:

            if segment.__class__.__name__ == "Arc":
                arc_count += 1

        if arc_count == 2:
            return "Circle"


    # Polygon classification

    if segments == 3:
        return "Triangle"

    elif segments == 4:
        return "Quadrilateral"

    elif segments == 5:
        return "Pentagon"

    elif segments == 6:
        return "Hexagon"

    else:
        return "Unknown"