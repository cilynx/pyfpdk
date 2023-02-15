#!/usr/bin/env python3

from pyfpdk import Room

room = Room([(0,0), (0,10*12), (8*12,8*12), (10*12,0)])
room.walls[2].addDoor(left_d=2*12)
room.write_svg()
