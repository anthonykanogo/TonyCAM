import os

from tonycam.svg_reader import read_svg
from tonycam.gcode_writer import generate_gcode
from tonycam.postprocessors.hycut import save_gcode
from tonycam.inspector import inspect_paths
from tonycam.contour import analyze_contours



INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"


# Find all SVG files
svg_files = []

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".svg"):
        svg_files.append(filename)


print("TonyCAM")
print("--------------------")
print(f"Found {len(svg_files)} SVG files")


# Process each SVG file
for svg_file in svg_files:

    input_path = os.path.join(INPUT_FOLDER, svg_file)

    name_without_extension = os.path.splitext(svg_file)[0]

    output_path = os.path.join(
        OUTPUT_FOLDER,
        name_without_extension + ".cnc"
    )


    paths = read_svg(input_path)
    
    contours = analyze_contours(paths)
    
    
    inspect_paths(paths)

    gcode = generate_gcode(contours)

    save_gcode(gcode, output_path)


    print(f"Processed: {svg_file}")
    print(f"Saved: {output_path}")