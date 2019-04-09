import threading

class DBController:
    
    def __init__(self):
        self.driver_address = None #String
        self.ipv4_address = None #String
        self.id = None #String
        self.password = None #String

        self.locker = threading.Lock()
        
    def update(self):
        self.locker.acquire()
        # ...
        self.locker.release()
        pass
    
    def select(self):
        self.locker.acquire()
        # ...
        self.locker.release()
        pass
    
    def delete(self):
        self.locker.acquire()
        # ...
        self.locker.release()
        pass
    
    def insert(self):
        self.locker.acquire()
        # ...
        self.locker.release()
        pass