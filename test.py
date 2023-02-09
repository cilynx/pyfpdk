#!/usr/bin/env python3

from pyfpdk import Room

for room in [Room([(0,0), (0,5), (4,4), (5,0)]), Room(10,20)]:
    print(room)
    print(room.area)
    print(room.points)
    for wall in room.walls:
        print(wall)
        print(wall.left, wall.right)
        print(wall.length)
