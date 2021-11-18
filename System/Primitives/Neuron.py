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

    def Output(self):
        self.Axon.Output()

    def Input(self, value):
        self.Potential += value
        self._checkPotential()
    
    def _checkPotential(self):
        if self.Potential >= self.Threshold:
            self.Output()
    
    def _potentialDecay(self):
        environment_modulation = self.Environment.getCondition()
        potential = self.Potential
        new_potential = self.Potential * environment_modulation
        self.Potential = new_potential
