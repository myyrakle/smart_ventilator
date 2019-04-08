from db_control import DBController
from fan_control import FanController

class SensingHandler:

    def __init__(self, fan, db):
        self.co2_pin #Integer
        self.co_pin #Integer
        self.pm_pin #Integer
        
        self.co2_value #Float
        self.co_value #Flaot
        self.pm1_value #Float
        self.pm2_value #Float
        self.pm3_value #Float
        
        self.db_controller = fan #DBController
        
        self.fan_controller = db #FanController
    
    def start():
        pass