class Axon:
    ''' Model Axon Primitive \n
    Axon functions as a sendeer of signals to External Source: Dendrite \n
    Each Axon receives a neuron which it belongs to \n
    '''
    def __init__(self, neuron, synapses=None):
        self.Neuron = neuron
        self.Synapses = synapses
        self.ID = self.Neuron.ID

    def addSynapse(self, synapse):
        if self.Synapses is None:
            self.Synapses = []
        self.Synapses.append(synapse)

    def Output(self):
        for synapse in self.Synapses:
            synapse.Signal()
    
    def isSynapseAdded(self, synapse_id):
        return True # placeholder code

class MotorAxon(Axon):
    def __init__(self, neuron, action, synapse=None):
        self.Action = action
        super.__init__(neuron, synapse)
    
    def Output(self):
        self.Action()
    