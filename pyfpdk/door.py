class Door():

    ############################################################################
    # Initializer
    ############################################################################

    def __init__(self, wall, left_d=None, right_d=None, width=24, swing="in"):
        if left_d is not None:
            if right_d is not None:
                raise Exception("Specify distance from left or right but not both")
            else:
                self.left_d = left_d
                self.right_d = wall.width - left_d - width
        if right_d is not None:
            self.right_d = right_d
            self.left_d = wall.width - right_d - width

        self.width = width
        self.swing = swing
        self.wall = wall
        self.mate = None

        print(self.left, self.right)

        wall.drawing.add(wall.drawing.path(d=f"M {self.left[0]} {self.left[1]} L {self.right[0]} {self.right[1]}", fill="white", stroke="red"))

    ############################################################################
    # Geometry
    ############################################################################

    @property
    def slope(self):
        return self.wall.slope

    @property
    def left(self):
        x = self.wall.left[0] + (self.left_d / self.wall.width) * (self.wall.right[0]-self.wall.left[0])
        y = self.wall.left[1] + (self.left_d / self.wall.width) * (self.wall.right[1]-self.wall.left[1])
        return (x,y)

    @property
    def right(self):
        x = self.wall.right[0] + (self.right_d / self.wall.width) * (self.wall.left[0]-self.wall.right[0])
        y = self.wall.right[1] + (self.right_d / self.wall.width) * (self.wall.left[1]-self.wall.right[1])
        return (x,y)
