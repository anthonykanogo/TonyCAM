from tonycam.svg_reader import read_svg
from tonycam.gcode_writer import generate_gcode
from tonycam.postprocessors.hycut import save_gcode


SVG_FILE = "input/square.svg"
OUTPUT_FILE = "output/square.cnc"


paths = read_svg(SVG_FILE)

gcode = generate_gcode(paths)

save_gcode(gcode, OUTPUT_FILE)

print("TonyCAM")
print("--------------------")
print(f"Loaded : {SVG_FILE}")
print(f"Paths  : {len(paths)}")
print(f"Saved  : {OUTPUT_FILE}")