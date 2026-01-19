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
        self.auto_mode = True
        self.force_state = None

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
    
    def handle_command(self, cmd: str):
        if cmd == "auto":
            self.auto_mode = True
            self.force_state = None
            print("Switched to automatic mode.")
        elif cmd in ["red", "green", "yellow"]:
            self.auto_mode = False
            self.force_state = TrafficLightState[cmd.upper()]
            self.state = self.force_state
            self.state_started = time.time()
            print(f"Forced state to: {self.state.name}")
    
    def check_for_input(self):
        import select, sys
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    def run(self):
        print("Traffic light system started. Type 'auto', 'red', 'green', or 'yellow' to control.")
        while True:
            now = time.time()
            if self.auto_mode:
                if self.update(now):
                    print(f"State changed to: {self.state.name}")
            else:
                if self.force_state and self.state != self.force_state:
                    self.state = self.force_state
                    self.state_started = now
                    print(f"State forced to: {self.state.name}")
            time.sleep(0.1)
            if self.check_for_input():
                cmd = input().strip().lower()
                self.handle_command(cmd)
        

if __name__ == "__main__":
    traffic_light = TrafficLight()
    traffic_light.run()