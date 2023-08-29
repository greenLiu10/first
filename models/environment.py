class traffic_env:
    def __init__(self, network_file, congested=[], traffic_light=[], evaluation="", congestion_level="",
                 travel_speed=0):
        self.travel_speed = travel_speed
        self.congestion_level = congestion_level
        self.evaluation = evaluation
        self.traffic_light = traffic_light
        self.congested = congested
        self.network_file = network_file
