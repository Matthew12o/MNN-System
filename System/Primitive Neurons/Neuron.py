
class Neuron:
    def __init__(self, id, environment, dendrites=None, axons=None):
        self.ID = id
        self.Environment = environment
        self.Dendrites = dendrites
        self.Axons = axons
        self.Potential = 0
        self.Threshold = 0
    
    def setThreshold(self, value):
        self.Threshold = value

    def addDendrite(self, dendrite):
        self.Dendrites.append(dendrite)
    
    def addAxon(self, axon):
        self.Axons.append(axon)

    def Output(self):
        for axon in self.Axons:
            axon.Output()

    def Input(self, value):
        self.Potential += value
        self._checkPotential()
    
    def _checkPotential(self):
        if self.Potential >= self.Threshold:
            self.Output()
        
        
class Dendrite:
    def __init__(self, id, neuron):
        self.ID = id
        self.Neuron = neuron


    def receiveSignal(self, axon_id):
        self._processSignal(axon_id)
    
    def _processSignal(self, axon_id):
        return 0
        
    
class Axon:
    def __init__(self, id, neuron, dendrites):
        self.ID = id
        self.Neuron = neuron
        self.Dendrites = dendrites
    def Output(self):
        for dendrite in self.Dendrites:
            dendrite.ReceiveSignal(self.ID)



    