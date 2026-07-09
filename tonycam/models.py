class Contour:

    def __init__(self, path):

        self.path = path

        # Geometry information
        self.segments = len(path)

        self.closed = (
            path[0].start == path[-1].end
        )

        self.shape = None

        self.width = None
        self.height = None


        # User selection
        self.selected = True


        # CAM information
        self.operation = "CUT"

        self.priority = 0

        self.role = "UNKNOWN"


        # Topology information
        self.parent = None

        self.children = []