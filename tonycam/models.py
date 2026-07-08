class Contour:

    def __init__(self, path):

        self.path = path

        self.segments = len(path)

        self.closed = (
            path[0].start == path[-1].end
        )

        self.shape = None

        self.width = None
        self.height = None

        self.selected = True