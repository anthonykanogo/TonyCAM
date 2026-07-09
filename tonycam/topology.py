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


    # Assign roles

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
    Temporary containment test.

    Uses dimensions only.
    Will be replaced with true geometry analysis.
    """

    if inner.width is None or outer.width is None:
        return False


    if inner.height is None or outer.height is None:
        return False


    return (
        inner.width < outer.width
        and
        inner.height < outer.height
    )