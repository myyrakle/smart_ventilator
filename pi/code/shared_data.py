import threading

class SharedData:
    
    def __init__(self):
        self.last_sensing = {}
        self.auto_mode = True
        self.locker = threading.Lock()
        pass
    
    
    def set_sensing(self, pm10, pm25, co, co2):
        self.locker.acquire()
        
        self.last_sensing['pm10']=pm10
        self.last_sensing['pm25']=pm25
        self.last_sensing['co']=co
        self.last_sensing['co2']=co2
        
        self.locker.release()
        pass
    
    
    def get_sensing(self):
        
        return self.last_sensing

datas = SharedData()