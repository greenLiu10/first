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

    
    step_length = 0.1  
    segment_length = 85.0  
    current_time = 0.0

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

        current_time += step_length

        if current_time >= segment_length:
            vehicle_info = agent.collect_vehicle_info()
            state = agent.extract_state_from_vehicle_info(vehicle_info)
            # 收集车辆信息并传递给决策车辆
            # vehicle_info = collect_vehicle_info()  # 自定义方法，收集车辆信息
            # make_decision(vehicle_info)  # 自定义方法，传递信息给决策车辆
            
            for vehicle_id, info in vehicle_info.items():
                action = agent.make_decision(state)
                # 根据action确定车辆的路径，并在SUMO中进行相应操作
                reward = ...  # 根据仿真结果计算奖励
                next_state = ...  # 根据仿真结果计算下一个状态
                agent.update_q_values(state, action, reward, next_state)

            # 重置时间和信息
            current_time = 0.0

    # 关闭 SUMO
    traci.close()


    # step = 0
    # while step < 1000:
    #     traci.simulationStep()
        
    #     vehicle_ids = traci.vehicle.getIDList()
    #     for vehicle_id in vehicle_ids:
    #         vehicle_lane = traci.vehicle.getLaneID(vehicle_id)
    #         vehicle_speed = traci.vehicle.getSpeed(vehicle_id)
    #         print(f"Vehicle ID: {vehicle_id}, Lane: {vehicle_lane}, Speed: {vehicle_speed}")

    #     step += 1
        
    # traci.close()
    
    