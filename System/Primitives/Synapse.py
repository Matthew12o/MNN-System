class Synapse:
    '''
    Model Synapse Primitive \n
    Synapse functions as a modulator of the communication between the Axon and the Dendrite
    '''
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
        '''Receives Signal from Axon'''
        raw_signal = self.DefaultSignal
        modulated_signal = self._ExternalModulation(raw_signal)
        return modulated_signal

    
    def _ExternalModulation(self, raw_signal):
        ''' External Modulation \n 
        In default state, does not do anything
        '''
        environment_values = self.Environment.getCondition()
        return raw_signal
