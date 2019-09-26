from room import Room
from key import Key
from door import Door

class Adventure:

    def __init__(self):
        self.rooms = []
        self.currentRoom = 0
        self.inventory = []

        firstRoom = Room(1,"Je staat in de keuken. Er zijn 2 sleutels, een met het label '0', en een met het label '1'. Er is maar 1 deur.", [Door(123, 1)], [Key(123),Key(321)])
        secondRoom = Room(2,"Je staat in de woonkamer, er is een deur", [Door(123, 0)], [])
        self.rooms.append(firstRoom)
        self.rooms.append(secondRoom)
        "huidige kamer is: " + self.rooms[self.currentRoom].description


    def pickupKey(self, _key):

        self.inventory = self.rooms[self.currentRoom].keys.pop(_key)


    def openDoor(self, _door, _key):

        if self.rooms[self.currentRoom].keys[_key].keyCode == self.rooms[self.currentRoom].doors[_door].unlockCode:
            self.currentRoom = self.rooms[self.currentRoom].doors[_door].leadsTo
            result = "deur opent."

        else:
            result = "deur opent niet."

        return (result + " huidige kamer is: " + self.rooms[self.currentRoom].description)


theGame = Adventure()


while True:
    keyToUse = int(input( "Welke wil je gebruiken?"))
    print(theGame.openDoor(0,keyToUse))

