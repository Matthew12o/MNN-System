from System.Primitives.NetworkEngine import NetworkEngine

class Cluster:
    '''Primitive Cluster \n
    All clusters will be inherited from the model cluster \n
    '''
    def __init__(self, id):
        self.ID = id
        self.Neurons = []
    
    def addNeurons(self, neuron):
        self.Neurons.append(neuron)
    
    def connectNeurons(self, connection_data):
        NE = NetworkEngine()
        network_data = NE.parseNetworkData(file_path)
        
            

    
