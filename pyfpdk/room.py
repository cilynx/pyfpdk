from .wall import Wall

class Room():

    ############################################################################
    # Initializer
    ############################################################################

    def __init__(self, arg1, y=None):
        if y is not None:
            self.points = [(0,0), (0,y), (arg1,y), (arg1,0)]
        else:
            self.points = arg1

        # Assumes points are in clockwise order.  The resulting Wall array will
        # be in clockwise order starting with the wall with the first point on
        # the left.
        self.walls = []
        for i in range(len(self.points)-1):
            self.walls.append(Wall(self.points[i], self.points[i+1]))
        self.walls.append(Wall(self.points[i+1], self.points[0]))

    ############################################################################
    # Area
    ############################################################################

    @property
    def area(self):
        count = len(self.points)
        area = 0.0
        for i in range(count):
            j = (i + 1) % count
            area += self.points[i][0] * self.points[j][1]
            area -= self.points[j][0] * self.points[i][1]
        area = abs(area) / 2.0
        return area
