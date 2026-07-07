from svgpathtools import svg2paths


def read_svg(filename):
    """
    Read an SVG file and return its paths.
    """
    paths, attributes = svg2paths(filename)
    return paths