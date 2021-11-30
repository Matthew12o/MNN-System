from Python.Environment.DataFeedEngine.External_API.DataFeedEngine import DataFeedEngine
from Python.Environment.DataFeedEngine.SimulationEngine.Simulation_Repository import SimulationRepository

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


