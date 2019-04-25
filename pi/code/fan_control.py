import threading
import RPi.GPIO as GPIO

class FanController:
    
    def __init__(self):
        self._is_on = False
        
        self.pin_number = 21 #Integer
        
        self.locker = threading.Lock()
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_number, GPIO.OUT)
        pass #pin_number=pin
    
    def on(self):
        #self.locker.acquire()
        print('pre')
        self._is_on = True
        GPIO.output(self.pin_number, True)
        print('aft')
        #self.locker.release()
        pass # on fan
    
    def off(self):
        #self.locker.acquire()
        
        self._is_on = False
        GPIO.output(self.pin_number, False)
        
        #self.locker.acquire()
        pass # off fan
    
    def is_on(self):
        return self._is_on