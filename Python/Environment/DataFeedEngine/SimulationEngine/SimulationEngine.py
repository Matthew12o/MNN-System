from Python.Environment.DataFeedEngine.External_API.DataFeedEngine import DataFeedEngine
from Python.Environment.DataFeedEngine.SimulationEngine.Simulation_Repository import SimulationRepository

import numpy as np
from enum import Enum

class SimulationEngine(DataFeedEngine):
    def __init__(self):
        self.SimulationRepository = SimulationRepository()
        super.__init__()
    
    def getSimulationData(self, simulation_reference):
        self.Simulation.append(simulation_reference)
    
    def createSimulation(self, simulation_reference, save=True):
        # Create Simulation
        sim_data = None # Placeholder

        # Upload Simulation
        if save:
            # Async save to Simulation Repository
            self.SimulationRepository.saveToSimulationRepository(simulation_reference, sim_data)

        return sim_data

    def _propagation(self, simulation_reference, benchmark=None):
        # get stat against benchmark
        targets_all = simulation_reference.Universe
        if not benchmark is None:
            targets_all = targets_all.append(benchmark)

        # check for data
        # if data available then check for
            
        # if not available then request data 

        # get stats against benchmark if benchmark is available
        stat_parameters = {}
        if not benchmark is None:
            for security in simulation_reference.Universe:
                stat_parameters[security.ID] = self._generate_stat_variables(security, benchmark)
        
        corr = self._getCorrelationMatrix(simulation_reference.Unvierse)

        # generate simulations
        r_v = self._generate_random_variables(len(simulation_reference.Universe), simulation_reference.getSimulationLength(), 0)

        simulation = {}
        i = 0
        for security in simulation_reference.Universe:
            simulation[security] = self._getSimulatedPrice(security, r_v[i])
            i += 1
        return simulation

    def _generate_stat_variables(security, benchmark):
        variables = 0 
        return variables

    def _generate_random_variables(self, n_securities, length, distribution_type):
        W = np.array()
        for n in n_securities:
            if distribution_type == 0: # Gaussian
                d = np.random.normal(0, 1, length) 
            # Include more distribution types
            W.append(d)
        return W
    
    def _adjustRandomVariableForCorrelation(W, corr):
        matrix = [] # Placeholder
        return matrix
    
    def _getSimulatedPrice(self, universe, random_variable):
        price_series = []
        for i in range(0, len(random_variable)):
            if i == 0:
                price_series.append(0) # replace with asset valuation model 
            else:
                price_series.append(0) # replace with asset valuation model
        return price_series
    
    def _getCorrelationMatrix(self, universe):
        corr_matrix = 0
        return corr_matrix

class DistributionType(Enum):
    Gaussian=0
    Binomial=1
    Beta=2
    Exponential=3
            

class SimulationReference:
    def __init__(self, id, description, univ, start_epoch, length, **kwargs):
        self.ID = id
        self.Description = description
        self.Start = start_epoch
        self.End = start_epoch + length
        self.Universe = univ
    
    def getSimulationLength(self):
        return self.End - self.Start
    

        
