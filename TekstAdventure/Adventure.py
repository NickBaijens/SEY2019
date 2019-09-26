from room import Room
from key import Key
from door import Door

rooms = []
currentRoom = 0

firstRoom = Room(1,"een keuken", [Door(123, 1)], [Key(123),Key(321)])
secondRoom = Room(2,"een woonkamer", [Door(123, 0)], [])
rooms.append(firstRoom)
rooms.append(secondRoom)

doorToOpen = 0
keyToUse = 1

if rooms[currentRoom].keys[keyToUse].openDoor(rooms[currentRoom].doors[doorToOpen]):
    currentRoom = rooms[currentRoom].doors[doorToOpen].leadsTo
    result = "deur opent."
else:
    result = "deur opent niet."
print(result + " huidige kamer is: " + rooms[currentRoom].description)

