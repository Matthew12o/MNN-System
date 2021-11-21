
class External_API:
    def __init__(self):
        self.isActive = False
    
    def Connect(self):
        self.isActive = True
    
    def getStatus(self):
        return self.isActive, 0