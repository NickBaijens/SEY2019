from room import Room
from key import Key
from door import Door

class Adventure:
    def __init__(self):
        firstRoom = Room("keuken","dit is een keuken", [Door(123)], [Key(123),Key(321)])
        secondRoom = Room("woonkamer","dit is een woonkamer", [Door(123)], [])

