
class Neuron:
    def __init__(self, id, environment, dendrites=None, axons=None):
        self.ID = id
        self.Environment = environment
        self.Dendrites = dendrites
        self.Axons = axons
        self.Potential = 0
        self.Threshold = None
    
    def setThreshold(self, value):
        self.Threshold = value

    def addDendrite(self, dendrite):
        if self.Dendrites is None:
            self.Dendrites = []
        self.Dendrites.append(dendrite)
    
    def addAxon(self, axon):
        if self.Axons is None:
            self.Axons = []
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
    def __init__(self, id, neuron, synapses=None):
        self.ID = id
        self.Neuron = neuron
        self.Synapses = synapses

    def receiveSignal(self, signal, synapse_id):
        self.Environment.
        self._processSignal(signal)
    
    def _processSignal(self, signal):
        return 0 # Placeholder

    def addSynapse(self, synapse):
        if self.Synapses is None:
            self.Synapses = []
        self.Synapses.append(synapse)

class Axon:
    def __init__(self, id, neuron, synapses=None):
        self.ID = id
        self.Neuron = neuron
        self.Synapses = synapses

    def Output(self):
        for dendrite in self.Dendrites:
            dendrite.ReceiveSignal(self.ID)

    def addSynapse(self, synapse):
        if self.Synapses is None:
            self.Synapses = []
        self.Synapses.append(synapse)

class Synapse:
    def __init__(self, dendrite, axon, environment, isInhibitory=False, default_signal=1):
        self.Dendrite = dendrite
        self.Axon = axon
        self.isInhibitory = isInhibitory
        self.Environment = environment
        self.DefaultSignal = default_signal
        
    def Signal(self):
        raw_signal = self.DefaultSignal
        modulated_signal = self._ExternalModulation(self, raw_signal)
        return 0 # Placeholder
        # self.Dendrite.receiveSignal()

    def _ExternalModulation(self, raw_signal):
        environement_condition = self.Environment
        # do something with the modulation
        


        