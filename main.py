from svgpathtools import svg2paths

filename = "input/square.svg"

paths, attributes = svg2paths(filename)

print("--------------------------------")
print("TonyCAM SVG Reader")
print("--------------------------------")
print(f"File : {filename}")
print(f"Number of paths : {len(paths)}")

for i, path in enumerate(paths):
    print(f"\nPath {i+1}")
    print(path)