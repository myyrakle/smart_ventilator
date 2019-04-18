import threading

class FanController:
    
    def __init__(self):
        self.pin_number = None #Integer
        self.locker = threading.Lock()
        pass #pin_number=pin
    
    def on(self):
        self.locker.acquire()
        # ...
        self.locker.release()
        pass # on fan
    
    def off(self):
        self.locker.acquire()
        # ...
        self.locker.acquire()
        pass # off fan