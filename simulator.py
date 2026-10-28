"""Hardware-free simulator; not the original thesis software."""
import sys
from src.commands import DEVICES, decode

class SmartHomeSimulator:
    def __init__(self):
        self.state = {name: False for key, name in DEVICES.items() if key != '55'}

    def apply(self, command):
        device, on = decode(command)
        if command[:2] == '55':
            for key in self.state:
                self.state[key] = on
        else:
            self.state[device] = on
        return {"command": command, "target": device, "on": on, "feedback": 1111}

if __name__ == '__main__':
    sim = SmartHomeSimulator()
    for command in sys.argv[1:] or ['100', '105', '000', '005']:
        try:
            print(sim.apply(command))
        except ValueError as exc:
            print(f'{command}: {exc}', file=sys.stderr)
            sys.exit(1)
    print('Final state:', sim.state)
