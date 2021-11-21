from Python.System.Primitives.Synapse import Synapse
from System.Primitives.NetworkEngine import NetworkEngine

class Cluster:
    '''Primitive Cluster \n
    All clusters will be inherited from the model cluster \n
    '''
    def __init__(self, id, environment):
        self.ID = id
        self.Environment = environment
        self.Neurons = {}
        self.Synapses = {}
    
    def addNeuron(self, neuron):
        self.Neurons[neuron.ID] = neuron
    
    def addSynapse(self, synapse):
        self.Synapses[synapse.ID] = synapse

    def connectNeurons(self, file_path):
        NE = NetworkEngine(self.Environment)
        neurons, synapses = NE.parseNetworkData(file_path)
        self.Neurons = neurons
        self.Synapses = synapses
        
    def removeNeuron(self, neuron_id):
        neuron = self.Neurons[neuron_id]
        axon = neuron.Axon
        dendrite = neuron.Dendrite
        
        # remove synapse connected to axon
        for synapse in axon.Syanpses:
            self.removeSynapse(synapse.ID)
        
        # remove synapse connected to dendrite
        for synapse in dendrite.Synapses:
            self.removeSynapse(synapse.ID)

        # remove neuron
        temp_dict = self.Neurons
        del temp_dict[neuron_id]
        self.Neurons = temp_dict
    
    def removeSynapse(self, synapse_id):
        temp_dict = self.Synapses
        del temp_dict[synapse_id]
        self.Synapses = temp_dict    

    
