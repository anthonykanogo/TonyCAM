from svgpathtools import svg2paths

filename = "input/square.svg"

paths, attributes = svg2paths(filename)

print("=" * 45)
print("TonyCAM Geometry Inspector")
print("=" * 45)

for path_number, path in enumerate(paths, start=1):

    print(f"\nPATH {path_number}")

    for segment_number, segment in enumerate(path, start=1):

        start = segment.start
        end = segment.end

        print(f"\nSegment {segment_number}")
        print(f"Type : {type(segment).__name__}")
        print(f"Start: ({start.real:.2f}, {start.imag:.2f})")
        print(f"End  : ({end.real:.2f}, {end.imag:.2f})")