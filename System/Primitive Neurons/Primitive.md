# Primitive Neuron Documentation

Primitive Neurons are model neurons. Neurons in MNN and CMN will inherit from model neurons and changed to fit its particular function.

## Neuron Primitive
Basic Neuron all neurons are modeled after this module and will inherit it

Neuron Components:
1. Neuron
Neuron checks if its axon should activate or not
- key variables:
    - id
    - axons
    - dendrites
    - threshold
    - signal types/frequencies

2. Dendrite
Dendrite receives signal/data from axons and sends fixed amount of potential to the Neuron. The signal received by axon is modulated by the environment. Dendrite will contain the connection information
- key variables:
    - id
    - external axons
        - each external axon contains its own signal value (excitatory vs inhibitory)
    - environment modulation
    
3. Axon
- key variables:
    - id
    - signal value

Axon receives activation signal from the neuron and sends a fixed signal to any dendrite avaiable. 