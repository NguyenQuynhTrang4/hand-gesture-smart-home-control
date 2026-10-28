"""Documented commands from the 2023 thesis, with noted ambiguity."""
DEVICES = {
    "10": "Floor 1 lights and fan",
    "11": "Floor 1 television and fan",
    "20": "Floor 2 television",
    "21": "Floor 2 lights and fan",
    "30": "Floor 3 lights and fan",
    "31": "Garden lights and fan",
    "00": "Garage gate",
    "55": "All devices",
}

def decode(command: str):
    if len(command) != 3 or not command.isdigit() or command[:2] not in DEVICES or command[2] not in '05':
        raise ValueError('Expected a documented three-digit command ending in 0 (ON) or 5 (OFF)')
    return DEVICES[command[:2]], command.endswith('0')
