"""
Implements sensor class
"""

class Sensor:
    def __init__(self, sensor_name=None, sensor_type: str=""):
        self._sensor_name = sensor_name
        self._sensor_id = None
        self._sensor_type: str = sensor_type
        self._dependencies = set()

    def create_sensor(self, sensor_name: str, sensor_type: str):
        pass

    def create_sensor_table(self):
        pass

