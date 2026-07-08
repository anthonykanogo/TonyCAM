def analyze_contours(paths):

    print("")
    print("=============================================")
    print("TonyCAM Contour Analyzer")
    print("=============================================")

    for index, path in enumerate(paths):

        first_point = path[0].start
        last_point = path[-1].end

        closed = first_point == last_point

        print("")
        print(f"Contour {index + 1}")
        print("----------------------------")

        print(f"Closed : {closed}")
        print(f"Segments: {len(path)}")

        print(
            f"Start: ({first_point.real:.2f}, {first_point.imag:.2f})"
        )

        print(
            f"End  : ({last_point.real:.2f}, {last_point.imag:.2f})"
        )