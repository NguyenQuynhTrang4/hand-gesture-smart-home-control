import unittest
from src.commands import decode
from src.simulator import SmartHomeSimulator

class SimulatorTests(unittest.TestCase):
    def test_on_off(self):
        sim = SmartHomeSimulator()
        sim.apply('100')
        self.assertTrue(sim.state['Floor 1 lights and fan'])
        sim.apply('105')
        self.assertFalse(sim.state['Floor 1 lights and fan'])

    def test_all_on_off(self):
        sim = SmartHomeSimulator()
        sim.apply('550')
        self.assertTrue(all(sim.state.values()))
        sim.apply('555')
        self.assertFalse(any(sim.state.values()))

    def test_bad_code(self):
        with self.assertRaises(ValueError):
            decode('999')

if __name__ == '__main__':
    unittest.main()
