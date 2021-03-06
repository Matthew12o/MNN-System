from Python.System.Primitives.Neuron import Neuron

class Dendrite:
    ''' Model Dendrite Primitive \n
    Dendrite functions as a receiver of signal from external sources: Axon\n
    Each Dendrite receives a neuron which it belongs to \n

    '''
    def __init__(self, neuron, synapses=None):
        self.Neuron = neuron
        self.Synapses = synapses
        self.ID = self.Neuron.ID

    def addSynapse(self, synapse):
        if self.Synapses is None:
            self.Synapses = []
        self.Synapses.append(synapse)

    def receiveSignal(self, signal, synapse_id):
        self.Environment.recordInteractions(signal, synapse_id)
        self._processSignal(signal)
    
    def isSynapseAdded(self, synapse_id):
        return True # Placeholder 
    
    def _processSignal(self, signal):
        return 0 # Placeholder

class SensoryNeuronDendrite(Dendrite):
    def __init__(self, neuron, external_stimuli, synapses=None):
        self.Stimuli = external_stimuli
        super.__init__(neuron, synapses)
    
    def receiveSignal(self, signal, stimuli_id):
        self.Environment.recordInteraction(signal, stimuli_id)
        self._processSignal(signal)
        