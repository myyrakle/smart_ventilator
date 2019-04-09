from fan_control import FanController
from socket_handle import SocketHandler
from sensing_handle import SensingHandler
from db_control import DBController

import threading

class MainHandler:
    
    def __init__(self):
        self.fan_controller = FanController()
        self.db_controller = DBController()

        self.socket_handler = SocketHandler(fan = self.fan_controller, db = self.db_controller)
        self.sensing_handler = SensingHandler(fan = self.fan_controller, db = self.db_controller)
        

    def run(self):

        # socket starts in other thread
        threading.Thread(target=self.socket_handler.start).start()
    
        # sensing starts in main thread
        self.sensing_handler.start()