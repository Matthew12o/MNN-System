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
        raw_signal = self.DefaultSignal
        modulated_signal = self._ExternalModulation(raw_signal)

        return 0 # Placeholder
        # self.Dendrite.receiveSignal()

    def _ExternalModulation(self, raw_signal):
        environement_condition = self.Environment
        # do something with the modulation
