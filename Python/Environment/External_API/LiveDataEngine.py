from Python.Environment.External_API.Bloomberg_API import BloombergAPI
from Python.Environment.External_API.IB_API import IB_API
from Python.Environment.External_API.DataFeedEngine import DataFeedEngine

class LiveDataEngine(DataFeedEngine):
    def __init__(self):
        self.API = []
        self.API.append(BloombergAPI())
        self.API.append(IB_API())
    
    def Connect(self, api_reference):
        self.API[api_reference].Connect()
    
    def getStatus(self, api_reference):
        return self.API[api_reference].isActive, self.API[api_reference].getStatus()
