def classify_shape(path):

    segments = len(path)

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