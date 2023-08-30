import os
import sys
import traci
import xml.etree.ElementTree as ET


sys.path.append('models/')
# from models import environment
from models import agent


def sumo_configuration():
    os.environ["SUMO_HOME"] = "C:/sumo-1.9.2"

    if 'SUMO_HOME' in os.environ:
        tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
        sys.path.append(tools)
    else:
        sys.exit("please declare environment variable 'SUMO_HOME'")


class StateSpace:
    def __init__(self):
        self.vehicles = {}  # 字典，存储车辆信息

    def add_vehicle(self, vehicle_id, vehicle_lane, vehicle_speed):
        self.vehicles[vehicle_id] = {
            "lane": vehicle_lane,
            "speed": vehicle_speed
        }

    def get_vehicle_info(self, vehicle_id):
        return self.vehicles.get(vehicle_id, None)

    def update_vehicle_info(self, vehicle_id, new_lane, new_speed):
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id]["lane"] = new_lane
            self.vehicles[vehicle_id]["speed"] = new_speed
        else:
            print("Vehicle not found in the state space.")

# 创建状态空间对象
state_space = StateSpace()

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
    while step < 86:
        traci.simulationStep()
        
        vehicle_ids = traci.vehicle.getIDList()
        for vehicle_id in vehicle_ids:
            vehicle_lane = traci.vehicle.getLaneID(vehicle_id)
            vehicle_speed = traci.vehicle.getSpeed(vehicle_id)

            state_space.add_vehicle(vehicle_id, vehicle_lane, vehicle_speed)
            print(f"state_space updated at step {step}: {vehicle_id, vehicle_lane,vehicle_speed}")
        
        step += 1
        
    traci.close()   