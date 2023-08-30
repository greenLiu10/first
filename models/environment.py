class StateSpace:
    def __init__(self):
        self.vehicles = {}  # 字典，存储车辆信息
        self.tls = {}


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
         
     
    def add_tl(self, tl_id, program_id):
        self.tls[tl_id] = {
            "program_id":program_id
        }  
    def get_tl_info(self, tl_id):
        return self.tls.get(tl_id, None)
            
    def update_tl_info(self, tl_id, program_id):
        if tl_id in self.tls:
            self.tls[tl_id]["signal"] = program_id
        else:
            print("Light not found in the state space.")

    def phase_to_ryg(phase_state):
    # 将相位状态字符串映射为 RYG 形式
        ryg_mapping = {
            "GGgg": "Green",
            "yy": "Yellow",
            "rrrr": "Red"
            # 可以根据实际需要继续添加其他状态的映射
    }
        ryg_state = " - ".join(ryg_mapping.get(state, "") for state in phase_state.split())
        return ryg_state