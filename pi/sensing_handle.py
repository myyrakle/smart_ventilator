from db_control import DBController
from fan_control import FanController

class SensingHandler:

    def __init__(self, fan, db):
        self.co2_pin = None #Integer
        self.co_pin = None #Integer
        self.pm_pin = None #Integer
        
        self.co2_value = None #Float
        self.co_value = None #Flaot
        self.pm1_value = None #Float
        self.pm2_value = None #Float
        self.pm3_value = None #Float
        
        self.db_controller = fan #DBController
        
        self.fan_controller = db #FanController
    
    def start(self):
        pass