import sys

from Python.Environment.Environment import Environment
from Python.Environment.DataFeedEngine.SimulationEngine.SimulationEngine import SimulationEngine
from Python.Environment.DataFeedEngine.External_API.LiveDataEngine import LiveDataEngine

def main(isTest=False):
    environment_id = 'Test Environment' if isTest else 'Live Environment'
    env = Environment(id=environment_id) 
    
    if isTest:
    # if test bringing in test environment data
        DataEngine = SimulationEngine()
    else:
    # if live environment connect to APIs
        DataEngine = LiveDataEngine()

    # Run until terminated
    isTerminated = False
    while not isTerminated:
        env.Run()

if __name__ == '__main__':
    sys.exit(main())