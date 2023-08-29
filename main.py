import os
import sys

import traci

sys.path.append('models/')
from models import environment
from models import agent

def sumo_configuration():
    os.environ["SUMO_HOME"] = "C:/sumo-1.9.2"

    if 'SUMO_HOME' in os.environ:
        tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
        sys.path.append(tools)
    else:
        sys.exit("please declare environment variable 'SUMO_HOME'")


if __name__ == '__main__':
    sumo_configuration()
    network_file = 'environments_files/network_files/two_crossing_connected.net.xml'
    flow_file = 'environments_files/flow_files/two_congested.rou.xml'
    
    env = environment.traffic_env(network_file, flow_file)

    sumoBinary = "C:/sumo-1.9.2/bin/sumo-gui"
    sumoCmd = [sumoBinary, "-c", "C:/Users/19388/Desktop/first/environments_files/first.sumocfg"]

    traci.start(sumoCmd)

    step = 0
    while step < 1000:
        traci.simulationStep()
        if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
            traci.trafficlight.setRedYellowGreenState("0", "GrGr")
            step += 1
    traci.close()
