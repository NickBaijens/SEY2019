class Key:
    def __init__(self, keyCode):
        self.keyCode = keyCode
    
    def openDoor(self, door):
        if(self.keyCode == door.unlockCode):
            return True
        else:
            return False