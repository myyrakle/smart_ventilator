import threading

class FanController:
    
    def __init__(self):
        self.pin_number #Integer
        self.locker = threading.Lock() #threading.Lock
        pass #pin_number=pin
    
    def on(self):
        pass # on fan
    
    def off(self):
        pass # off fan