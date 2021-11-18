
class Neuron:
    '''Model Neuron Primitive
    This class represents the simplest possible neuron. Other types of neurons will inherit Neuron class
    Required Parameters:
    - id: represents identifier
    - environment: represents environement
    Optional Parameters:
    - threshold: (default 1) represents the triggering threshold for neuron to activate.
    '''
    def __init__(self, id, environment, threshold=1):
        self.ID = id
        self.Environment = environment
        self.Potential = 0
        self.Threshold = threshold
        self.Axon = Axon('{}_Axon'.format(self.ID), self)
        self.Dendrite = Dendrite('{}_Dendrite'.format(self.ID), self)

    def setThreshold(self, value):
        self.Threshold = value

    def setDecayFactor(self, value):
        self.DecayFactor = value

    def Output(self):
        for axon in self.Axons:
            axon.Output()

    def Input(self, value):
        self.Potential += value
        self._checkPotential()
    
    def _checkPotential(self):
        if self.Potential >= self.Threshold:
            self.Output()
    
    def _potentialDecayFunction(self):
        environment_factors = self.Environment.getCondition()
        decay_factor = self.DecayFactor

class Dendrite:
    def __init__(self, id, neuron, synapses=None):
        self.ID = id
        self.Neuron = neuron
        self.Synapses = synapses

    def addSynapse(self, synapse):
        if self.Synapses is None:
            self.Synapses = []
        self.Synapses.append(synapse)

    def receiveSignal(self, signal, synapse_id):
        self.Environment.recordInteractions(signal, synapse_id)
        self._processSignal(signal)
    
    def checkSynapse(self, synapse_id):
        return True # Placeholder 
    
    def _processSignal(self, signal):
        return 0 # Placeholder

class Axon:
    def __init__(self, id, neuron, synapses=None):
        self.ID = id
        self.Neuron = neuron
        self.Synapses = synapses

    def addSynapse(self, synapse):
        if self.Synapses is None:
            self.Synapses = []
        self.Synapses.append(synapse)

    def Output(self):
        for dendrite in self.Dendrites:
            dendrite.ReceiveSignal(self.ID)
    
    def checkSynapse(self, synapse_id):
        return True # placeholder code
        
class Synapse:
    def __init__(self, dendrite, axon, environment, isInhibitory=False, default_signal=1):
        self.Dendrite = dendrite
        self.Axon = axon
        self.isInhibitory = isInhibitory
        self.Environment = environment
        self.DefaultSignal = default_signal
        self.ID = self._getID()
        
    def _getID(self):
        synapse_type = 'Inhibitory' if self.isInhibitory else 'Excitatory'
        identifier = '{} Synapse {} -> {}'.format(
            synapse_type, 
            self.Axon.ID,
            self.Dendrite.ID
        )
        return identifier

    def Signal(self):
        raw_signal = self.DefaultSignal
        modulated_signal = self._ExternalModulation(raw_signal)

        return 0 # Placeholder
        # self.Dendrite.receiveSignal()

    def _ExternalModulation(self, raw_signal):
        environement_condition = self.Environment
        # do something with the modulation



        