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
        self.state_started = time.time()

    def next_state(self):
        if self.state == TrafficLightState.RED:
            self.state = TrafficLightState.GREEN
        elif self.state == TrafficLightState.GREEN:
            self.state = TrafficLightState.YELLOW
        elif self.state == TrafficLightState.YELLOW:
            self.state = TrafficLightState.RED

    def update(self,now):
        elapsed = now - self.state_started
        if elapsed >= DURATION[self.state]:
            self.next_state()
            self.state_started = now
            return True
        else:
            return False

    def run(self):
        print(f"Starting traffic light simulation. Initial state: {self.state.name}")
        while True:
            now = time.time()
            if self.update(now):
                print(f"Traffic light changed to: {self.state.name}")
            time.sleep(0.1)

if __name__ == "__main__":
    traffic_light = TrafficLight()
    traffic_light.run()