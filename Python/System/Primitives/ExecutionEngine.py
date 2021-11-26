from Python.System.Primitives.Synapse import MotorMuscularJunction
from Python.Environment.DataFeedEngine.External_API.IB_API import IB_API

class ExecutionEngine:
    def __init__(self):
        self.API = IB_API
        self.DefaultOrder = None

    def addSynapse(self, MMJ):
        self.DefaultOrder = MMJ.DefaultOrder
    
    def Execute(self):
        self.API.sendOrder(self.DefaultOrder)
    
    def _getOrderConfirmation(self):
        return 0 # Placeholder

    def _getTradeConfirmation(self):
        return 0 # Placeholder
    
    