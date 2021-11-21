import json
import numpy as np
from Python.System.Primitives.Neuron import Neuron
from Python.System.Primitives.Synapse import Synapse

class NetworkEngine:
    def __init__(self, environment):
        self.Environment = environment

    def parseNetworkData(self, file_path):
        file = open(file_path)
        json_data = json.load(file)

        neuron_references = []
        for synapse in json_data['Synapses']:
            neuron_references.append(synapse['Dendrite'])
            neuron_references.append(synapse['Axon'])

        neurons = {}
        for reference in np.unique(np.array(neuron_references)):
            neurons[reference] = Neuron(reference, self.Environment)
        
        synapses = {}
        for synapse_reference in json_data['Synapses']:
            id = synapse_reference['ID']
            axon_ref = synapse_reference['Axon']
            dendrite_ref = synapse_reference['Dendrite']
            isInhibitory = synapse_reference['isInhibitory']
            magniture = synapse_reference['Magnitude']
            synapse[synapse_reference['ID']] = Synapse(
                dendrite = neurons[dendrite_ref].Dendrite,
                axon = neurons[axon_ref].Axon,
                environment = self.Environment,
                isInhibitory = isInhibitory,
                default_signal = magniture
            )
        
        return neurons, synapses


        


            
        
