from tonycam.geometry import contour_contains


def analyze_relationships(contours):

    print("")
    print("=============================================")
    print("TonyCAM Topology Analyzer")
    print("=============================================")


    # Reset relationships

    for contour in contours:
        contour.parent = None
        contour.children = []


    # Compare every contour against every other contour

    for contour in contours:

        for other in contours:

            # Don't compare itself
            if contour == other:
                continue


            if is_inside(contour, other):

                contour.parent = other
                other.children.append(contour)

                break


    # Assign roles based on topology

    for contour in contours:

        if contour.parent is None:
            contour.role = "OUTER PROFILE"

        else:
            contour.role = "INTERNAL FEATURE"


    # Display results

    for index, contour in enumerate(contours):

        print("")
        print(f"Contour {index + 1}")
        print("----------------------------")

        print(f"Shape: {contour.shape}")
        print(f"Role: {contour.role}")

        if contour.parent:

            print("Parent: Yes")

        else:

            print("Parent: None")


        print(f"Children: {len(contour.children)}")



def is_inside(inner, outer):

    """
    Determines whether one contour is inside another.

    Uses geometry analysis.

    Current version:
    Bounding-box containment.

    Future versions:
    True line/arc containment.
    """

    return contour_contains(
        outer,
        inner
    )
    