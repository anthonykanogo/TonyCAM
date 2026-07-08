from tonycam.dimensions import calculate_dimensions
from tonycam.shape import classify_shape
from tonycam.models import Contour


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


        # Display report
        print("")
        print(f"Contour {index + 1}")
        print("----------------------------")

        print(f"Closed : {contour.closed}")
        print(f"Segments: {contour.segments}")
        print(f"Shape: {contour.shape}")

        print(f"Width : {contour.width:.2f} mm")
        print(f"Height: {contour.height:.2f} mm")


        start = path[0].start
        end = path[-1].end

        print(
            f"Start: ({start.real:.2f}, {start.imag:.2f})"
        )

        print(
            f"End  : ({end.real:.2f}, {end.imag:.2f})"
        )


    return contours