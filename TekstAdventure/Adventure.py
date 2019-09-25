from room import Room
from key import Key
from door import Door
class Adventure:
    def __init__(self):
        doors = []
        keys = []
        doors.append(Door(123))
        keys.append(Key(123))
        keys.append(Key(321))
        firstRoom = Room("keuken","dit is een keuken", doors, keys)
