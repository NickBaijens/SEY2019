from room import Room
from key import Key
from door import Door

class Adventure:

    def __init__(self):
        self.rooms = []
        self.currentRoom = 0
        self.inventory = []

        firstRoom = Room(1,"Je staat in de keuken. Er staan een aanrecht en een koelkast, en er is 1 deur.", [Door(123, 1)], [Key(123,"woonkamersleutel"),Key(321,"schatkistsleutel")])
        secondRoom = Room(2,"Je staat in de woonkamer, er is een deur", [Door(123, 0)], [])
        self.rooms.append(firstRoom)
        self.rooms.append(secondRoom)
        print(self.rooms[self.currentRoom].description)


    def pickupKey(self, _key):

        self.inventory.append(self.rooms[self.currentRoom].keys.pop(_key))
        newItem = len(self.inventory)
        return self.inventory[newItem-1].label


    def openDoor(self, _door, _key):

        if _key.keyCode == _door.unlockCode:
            self.currentRoom = _door.leadsTo
            result = "deur opent. \n"

        else:
            result = "deur opent niet. \n"

        return (result + self.rooms[self.currentRoom].description)


theGame = Adventure()

kijkAanrecht = False
while True:
    inputVar = input( "Wat doe je?")
    
    if(inputVar == "kijk aanrecht"):
        kijkAanrecht = True
        print("Er ligt een sleutel op het aanrecht. ")
    elif(inputVar == "pickup" and kijkAanrecht==True):      
        print("je pakt " + theGame.pickupKey(0))

    elif(inputVar == "open deur" and theGame.inventory!= None):
        print(theGame.openDoor(theGame.rooms[theGame.currentRoom].doors[0], theGame.inventory[0]))
    
    elif(inputVar == "exit"):
        break

    elif(inputVar == "pickup" ):
        print("ik kan commando "+str(inputVar)+ " hier niet gebruiken")
    
    else:
        print("ik ken commando: "+inputVar+" niet.")
    

