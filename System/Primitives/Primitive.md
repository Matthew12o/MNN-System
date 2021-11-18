# Primitive Neuron Documentation

Primitive Neurons are model neurons. Neurons in MNN and CMN will inherit from model neurons and changed to fit its particular function.

## Neuron Primitive
Basic Neuron all neurons are modeled after this module and will inherit it

Neuron Components:
### 1. Neuron
#### Notes
- Simplifying Neurons to have one dendrite and axon each. While it would be more accurate to have multiple dendrites and axons to modulate each signals, the complexity it poses is to great and it'll also simply computation to use a single axon and dendrite. Modulation is done on the synaptic level, therefore, the interaction can occur without changing large portion of the function
#### Feature
Container for axons and dendrites. Checks/updates for its own potential and signals to axon for output if triggered.

#### Variables
Neuron checks if its axon should activate or not. 
- key variables:
    - id
    - axons
    - dendrites
    - threshold
    - signal types/frequencies

### 2. Dendrite
Dendrite receives signal/data from axons and sends fixed amount of potential to the Neuron. The signal received by axon is modulated by the environment. Dendrite will contain the connection information
- key variables:
    - id
    - external axons
        - each external axon contains its own signal value (excitatory vs inhibitory)
    - environment modulation

### 3. Axon
#### Feature

#### Variables
- key variables:
    - id
    - signal value

Axon receives activation signal from the neuron and sends a fixed signal to any dendrite avaiable. 

### 4. Synapse
#### Feature
Synapse represents connection between an Axon and a Dendrite. The environmental modulation also occurs in the synapse. 

#### Variables
- Dendrite
- Axon
- inhibitory or excitatory
- Environment

