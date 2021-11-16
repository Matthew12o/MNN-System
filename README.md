# MNN System
 MNN Trading System

Motor Neural Network Trading System is build based on muscular motor network. There are two major components: 1. motor neural network clusters and 2. centralized master neurons. With well designed network, it is possible to create a desired behavior heirarchy. MNN clusters are responsible for paricular behavior while CMN are responsible for modulating the system behavior. 

## System
### MNN-Cluster
Motor Neuron Network Cluster represents a subset of motor neurons that is responsible for a limited set of actions. Adding and substracting clusters will be equivalent to adding and subtracting functions to the application

### Central Master Neural Network
Central Master Neural Network takes information from external and internal sources to modulate the behavior of MNN-Clusters. 

### Environment
Environment represents the space in which the system operates. The environment is responsible for external data, and epoch management. Environment will interact with the system by inputting sensory data to the CMNN and receiving/sending data from the MNN-clusters. 

- Data
    - External API
- Epoch Management
- Simulation


## Optimization/Testing
Optimization and testing viability of the system will be performed by simulating a fake/past environments. Because MNN system is an input-output system, MNN will behave in a deterministic manner. 

### Genetic Algorithm
Provide the algorithm with all possible connections between the networks