def save_gcode(gcode, filename):

    with open(filename, "w") as file:
        file.write("\n".join(gcode))