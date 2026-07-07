def generate_gcode(paths):

    gcode = []

    gcode.append("; TonyCAM")
    gcode.append("; HyCut Prototype")
    gcode.append("")

    gcode.append("G21")
    gcode.append("G90")

    for path in paths:

        start = path[0].start

        gcode.append("")
        gcode.append(f"G0 X{start.real:.3f} Y{start.imag:.3f}")
        gcode.append("M03")

        for segment in path:

            end = segment.end
            gcode.append(f"G1 X{end.real:.3f} Y{end.imag:.3f}")

        gcode.append("M05")

    gcode.append("")
    gcode.append("M30")

    return gcode