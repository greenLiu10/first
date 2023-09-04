import os
import sys
import traci
import xml.etree.ElementTree as ET


sys.path.append('models/')
from models.environment import StateSpace


# from models import agent


def sumo_configuration():
    os.environ["SUMO_HOME"] = "C:/sumo-1.9.2"

    if 'SUMO_HOME' in os.environ:
        tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
        sys.path.append(tools)
    else:
        sys.exit("please declare environment variable 'SUMO_HOME'")


# 创建状态空间对象
state_space = StateSpace()
initial_state_size = len(state_space.tls)

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
        
        
    
    tree2 = ET.parse(network_file)
    root2 = tree2.getroot()

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
            print(f"state_space updated at step {step}: {vehicle_id, vehicle_lane, vehicle_speed}")

        tl_ids = traci.trafficlight.getIDList()
        for tl_id in tl_ids:
            program_id = traci.trafficlight.getProgram(tl_id)
            # 获取交通信号灯当前相位状态
            current_phase = traci.trafficlight.getPhase(tl_id)
            
            # 注意这里面的current_state指的不是每个车道上的红绿灯信息，而是顺时针方向，只以右侧通行的车道计数， 顺时针方向 每个 link 的通行信息，
            # 大写的G与小写的g体现了右行优先！！！！
            current_state = traci.trafficlight.getRedYellowGreenState(tl_id)
            # state_space.add_tl(tl_id, current_phase, current_state)

            print(f"Traffic_Light updated at step {step}: {tl_id, current_phase, current_state}")
        
   
        step += 1
    traci.close()
