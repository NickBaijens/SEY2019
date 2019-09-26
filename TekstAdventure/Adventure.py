from room import Room
from key import Key
from door import Door

firstRoom = Room(1,"dit is een keuken", [Door(123)], [Key(123),Key(321)])
secondRoom = Room(2,"dit is een woonkamer", [Door(123)], [])
result = "deur opent" if firstRoom.keys[0].openDoor(firstRoom.doors[0]) else "deur opent niet"

print(result)

