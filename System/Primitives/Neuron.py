from System.Primitives.Axon import Axon
from System.Primitives.Dendrite import Dendrite

class Neuron:
    '''Model Neuron Primitive \n
    This class represents the simplest possible neuron. Other types of neurons will inherit Neuron class
    Required Parameters: \n
    - id: represents identifier
    - environment: represents environement \n
    Optional Parameters: \n
    - threshold: (default 1) represents the triggering threshold for neuron to activate.
    '''
    def __init__(self, id, environment, threshold=1):
        self.ID = id
        self.Environment = environment
        self.Potential = 0
        self.Threshold = threshold
        self.Axon = Axon(self)
        self.Dendrite = Dendrite(self)

    def setThreshold(self, value):
        self.Threshold = value
    
    def _checkPotential(self):
        if self.Potential >= self.Threshold:
            self.Output()
    
    def _potentialDecay(self, decay_value=None):
        decay_value = self.Potential if decay_value is None else decay_value
        self.Potential = self.Potential - decay_value
        self._checkPotential()

    def Output(self):
        self._potentialDecay()
        self.Axon.Output()

    def Input(self, value):
        self.Potential += value
        self._checkPotential()