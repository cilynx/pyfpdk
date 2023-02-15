from .door import Door

class Wall():

    ############################################################################
    # Initializer
    ############################################################################

    def __init__(self, room, left, right):
        self.room = room
        self.left = left
        self.right = right
        self.doors = []

        self.drawing = room.drawing

        self.drawing.add(self.drawing.path(d=f"M {left[0]} {left[1]} L {right[0]} {right[1]}", fill="white", stroke="black"))

    ############################################################################
    # Geometry
    ############################################################################

    @property
    def width(self):
        return (((self.left[0]-self.right[0])**2)+((self.left[1]-self.right[1])**2))**0.5

    @property
    def slope(self):
        return (self.right[1]-self.left[1])/(self.right[0]-self.left[0])

    ############################################################################
    # Doors
    ############################################################################

    def addDoor(self, door=None, left_d=None, right_d=None):
        if door is None:
            door = Door(wall=self, left_d=left_d, right_d=right_d)
        self.doors.append(door)
        return door
