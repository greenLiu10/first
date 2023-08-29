import numpy as np
import sys
import datetime
import traci

class main_agent:
    
    def __init__(self, env, learning_rate, discounted_factor):
        self.env = env
        self.discounted_factor = discounted_factor
        self.learning_rate = learning_rate

    def collect_vehicle_info():
        
        vehicle_info = {}  # 创建一个字典来存储车辆信息
        vehicle_ids = traci.vehicle.getIDList()

        for vehicle_id in vehicle_ids:
            vehicle_lane = traci.vehicle.getLaneID(vehicle_id)
            vehicle_speed = traci.vehicle.getSpeed(vehicle_id)

            # 将车辆信息存储到字典中
            vehicle_info[vehicle_id] = {"lane": vehicle_lane, "speed": vehicle_speed}

        return vehicle_info
    
    def extract_state_from_vehicle_info(vehicle_info):
        state = []
        
        for vehicle_id, info in vehicle_info.items():
            vehicle_lane = info["lane"]
            vehicle_speed = info["speed"]

            # 将车辆状态信息添加到状态列表中
            state.extend([vehicle_lane, vehicle_speed])

        return state
    
    def make_decision(self, state):
        if np.random.rand() < self.exploration_prob:
            # 随机探索
            action = np.random.randint(self.num_actions)
        else:
            # 根据Q值选择动作
            action = np.argmax(self.q_table[state, :])

        return action

    def update_q_values(self, state, action, reward, next_state):
        current_q = self.q_table[state, action]
        max_next_q = np.max(self.q_table[next_state, :])
        new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (reward + self.discount_factor * max_next_q)
        self.q_table[state, action] = new_q
        
    # def update(self):
      #  self.q_table