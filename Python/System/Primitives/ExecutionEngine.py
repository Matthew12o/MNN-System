from Python.System.Primitives.Synapse import MotorMuscularJunction
from Python.Environment.DataFeedEngine.External_API.IB_API import IB_API

class ExecutionEngine:
    def __init__(self):
        self.API = IB_API
        self.DefaultOrder = None
        self.Order = None
    def addSynapse(self, MMJ):
        self.DefaultOrder = MMJ.DefaultOrder
    
    def Execute(self):
        self.API.sendOrder(self.DefaultOrder)
        # Async wait until order has been confirmed
        if self.isOrderConfirmed:
            return True

    def _isOrderConfirmed(self):
        self.Order = self.DefaultOrder
        return 0 # Placeholder

    def _isTradeConfirmed(self):
        # Async Function 
        return 0 # Placeholder
    
    def cancelOrder(self):
        return 0 # Placeholder 
        
    def outputTradeDeatils(self):
        return self.Order
        
    