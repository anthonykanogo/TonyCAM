def inspect_paths(paths):

    print("")
    print("=============================================")
    print("TonyCAM Geometry Inspector")
    print("=============================================")

    for index, path in enumerate(paths):

        print("")
        print(f"PATH {index + 1}")

        print("----------------------------")

        for number, segment in enumerate(path):

            print("")
            print(f"Segment {number + 1}")

            print(f"Type : {type(segment).__name__}")

            start = segment.start
            end = segment.end

            print(
                f"Start: ({start.real:.2f}, {start.imag:.2f})"
            )

            print(
                f"End  : ({end.real:.2f}, {end.imag:.2f})"
            )