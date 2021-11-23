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

    # Interacts with the Axon
    def Output(self):
        self._potentialDecay()
        self.Axon.Output()

    # Interacts with the Dendrite
    def Input(self, value):
        self.Potential += value
        self._checkPotential()

    # Interacts with the Environment    


class MasterNeuron(Neuron):
    def __init__(self, id, environment, threshold=1, sub=None):
        self.Subs = {} if sub is None else sub
        super.__init__(id, environment, threshold)

    def addSubNeuron(self, sub=None):
        if sub is None:
            self.addSubNeuron(self._createSubNeuron(len(self.Subs)))
        else:
            self.Subs[sub.ID] = sub
    
    def _createSubNeuron(self, id):
        sub = SubNeuron(id, self.Environment, self)
        return sub

    def modulateSubNeurons(self, value):
        for sub in self.Subs:
            sub.MasterNeuronModulation(value)
        

class SubNeuron(Neuron):
    def __init__(self, id, environment, master, threshold=1):
        self.Master = master
        super.__init__(id, environment, threshold)
    
    def MasterNeuronModulation(self, value):
        self.Input(value)

