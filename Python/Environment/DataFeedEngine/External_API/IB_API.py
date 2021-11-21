from Python.Environment.DataFeedEngine.External_API.API import External_API

class IB_API(External_API):
    def __init__(self):
        super.__init__()
    
    def Connect(self):
        ## initiate connection

        self.isActive = True
    
    def getStatus(self):
        ## Check API connection
        # self.Status 
        return self.Status
