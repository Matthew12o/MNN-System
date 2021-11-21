import pandas as pd

class Environment:
    def __init__(self, id, epoch=None):
        self.ID = id
        self.Epoch = 0 if epoch is None else epoch # Placeholder change 0 into a time value
        self.Data = {}

    def getCondition(self):
        condition = EnvironmentCondition(self.Epoch, self.Data)
        return condition

    def _updateEpoch(self):
        self.Epoch += 1

    def updateEnvironment(self, key, value):
        self.Data[key] = value

    def recordInteraction(self, interaction_data):
        # External Interaction

        # Synpaitc Formation

        # Synaptic Interaction
        
        # Cluster Formation

        # Cluster Interaction

        return 0 # Placeholder

class EnvironmentCondition:
    def __init__(self, epoch, condition_data):
        self.Epoch = epoch
        self.Data = pd.DataFrame.from_dict(condition_data)
    

