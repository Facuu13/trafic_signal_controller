import time
from enum import Enum

class TrafficLightState(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3

DURATION = {
    TrafficLightState.RED: 5,
    TrafficLightState.GREEN: 10,
    TrafficLightState.YELLOW: 2,
}

class TrafficLight:
    def __init__(self):
        self.state = TrafficLightState.RED

    def next_state(self):
        if self.state == TrafficLightState.RED:
            self.state = TrafficLightState.GREEN
        elif self.state == TrafficLightState.GREEN:
            self.state = TrafficLightState.YELLOW
        elif self.state == TrafficLightState.YELLOW:
            self.state = TrafficLightState.RED

    def run(self):
        while True:
            print(f"Traffic light is {self.state.name}")
            time.sleep(DURATION[self.state])
            self.next_state()

if __name__ == "__main__":
    traffic_light = TrafficLight()
    traffic_light.run()