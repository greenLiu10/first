class StateSpace:
    def __init__(self):
        self.vehicles = {}  # 存储车辆信息的字典
        self.tls = {}  # 存储红绿灯信息的字典

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

    def add_tl(self, tl_id, program_id, current_phase, current_state):
        self.tls[tl_id] = {
            "program_id": program_id,
            "current_phase": current_phase,
            "current_state": current_state
        }

    def get_tl_info(self, tl_id):
        return self.tls.get(tl_id, None)

    def update_tl_info(self, tl_id, program_id, current_phase, current_state):
        if tl_id in self.tls:
            self.tls[tl_id]["program_id"] = program_id
            self.tls[tl_id]["current_phase"] = current_phase
            self.tls[tl_id]["current_state"] = current_state

    def print_vehicles(self):
        print("Vehicle Information:")
        for vehicle_id, info in self.vehicles.items():
            print(f"Vehicle ID: {vehicle_id}")
            print(f"  Lane: {info['lane']}")
            print(f"  Speed: {info['speed']}")

    def print_tls(self):
        print("Traffic Light Information:")
        for tl_id, info in self.tls.items():
            print(f"Traffic Light ID: {tl_id}")
            print(f"  Program ID: {info['program_id']}")
            print(f"  Current Phase: {info['current_phase']}")
            print(f"  Current State: {info['current_state']}")
