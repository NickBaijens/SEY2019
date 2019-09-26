class Key:
    def __init__(self, _keyCode):
        self.keyCode = _keyCode
    
    def openDoor(self, door):
        if(self.keyCode == door.unlockCode):
            return True
        else:
            return False