from tonycam.dimensions import calculate_dimensions
from tonycam.shape import classify_shape
from tonycam.models import Contour


def assign_roles(contours):

    largest = max(
        contours,
        key=lambda c: c.width * c.height
    )

    for contour in contours:

        if contour == largest:
            contour.role = "OUTER PROFILE"
            contour.priority = 10

        else:
            contour.role = "INTERNAL FEATURE"
            contour.priority = 1



def analyze_contours(paths):

    contours = []

    print("")
    print("=============================================")
    print("TonyCAM Contour Analyzer")
    print("=============================================")

    for index, path in enumerate(paths):

        # Create a contour object
        contour = Contour(path)

        # Calculate geometry information
        contour.shape = classify_shape(path)

        contour.width, contour.height = calculate_dimensions(path)


        contours.append(contour)


    # Assign CAM roles after all contours are analyzed
    assign_roles(contours)


    # Display report
    for index, contour in enumerate(contours):

        path = contour.path

        print("")
        print(f"Contour {index + 1}")
        print("----------------------------")

        print(f"Closed : {contour.closed}")
        print(f"Segments: {contour.segments}")
        print(f"Shape: {contour.shape}")

        print(f"Width : {contour.width:.2f} mm")
        print(f"Height: {contour.height:.2f} mm")

        print(f"Priority: {contour.priority}")
        print(f"Operation: {contour.operation}")
        print(f"Role: {contour.role}")


        start = path[0].start
        end = path[-1].end

        print(
            f"Start: ({start.real:.2f}, {start.imag:.2f})"
        )

        print(
            f"End  : ({end.real:.2f}, {end.imag:.2f})"
        )


    return contours