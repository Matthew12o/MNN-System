
from Python.Environment.DataFeedEngine.External_API.Bloomberg_API import BloombergAPI
from Python.Environment.DataFeedEngine.External_API.IB_API import IB_API

from Python.Environment.DataFeedEngine.External_API.Bloomberg_API import BloombergAPI
from Python.Environment.DataFeedEngine.External_API.IB_API import IB_API

class DataFeedEngine:
    def __init__(self):
        self.API = []
        self.API.append(BloombergAPI())
        self.API.append(IB_API())
    
    def Connect(self, api_reference):
        self.API[api_reference].Connect()
    
    def getStatus(self, api_reference):
        return self.API[api_reference].isActive, self.API[api_reference].getStatus()
    
    def getAccountData(self):
        return None # placeholder
    
    def getMarketData(self):
        return None # placeholder

    def getPriceData(self):
        return None # placeholder