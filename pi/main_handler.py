import fan_control
import socket_handle
import sensing_handle

import threading

class MainHandler:
    fan_controller #FanController
    socket_handler
    sensing_handler
    
    __init__():
        fan_controller = fan_control.FanController()
        socket_handler = socket_handle.SocketHandler(fan_controller)
        sensing_handler = sensing_handle.SensingHandler(fan_controller)
        
    def run(self):
        socket_thread = threading.Thread(target=socket_handler.start)
        socket_thread.start()
        
        sensing_handler.start()