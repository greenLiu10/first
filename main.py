import os
import sys
import traci
import xml.etree.ElementTree as ET

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
    network_file = './environments_files/network_files/two_crossing_connected.net.xml'
    flow_file = './environments_files/flow_files/two_congested.rou.xml'
    
    tree = ET.parse(flow_file)
    root = tree.getroot()
    for vehicle_elem in root.findall('vehicle'):
        vehicle_id = vehicle_elem.get('id')
        vehicle_route = vehicle_elem.get('route')
        depart_time = vehicle_elem.get('depart')
        
        print(f"Vehicle ID: {vehicle_id}")
        print(f"Route ID: {vehicle_route}")
        print(f"Depart Time: {depart_time}")

    

    sumoBinary = "C:/sumo-1.9.2/bin/sumo-gui"
    sumoCmd = [sumoBinary, "-c", './environments_files/first.sumocfg']

    traci.start(sumoCmd)

    step = 0
    while step < 1000:
        traci.simulationStep()
        
        vehicle_ids = traci.vehicle.getIDList()
        for vehicle_id in vehicle_ids:
            vehicle_lane = traci.vehicle.getLaneID(vehicle_id)
            vehicle_speed = traci.vehicle.getSpeed(vehicle_id)
            print(f"Vehicle ID: {vehicle_id}, Lane: {vehicle_lane}, Speed: {vehicle_speed}")

        step += 1
        
    traci.close()
    
    