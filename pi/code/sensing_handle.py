from db_control import DBController
from fan_control import FanController

import mh_z19 as co2
import ze07_co_uart as co
import pms7003 as pm

import time

class SensingHandler:

    def __init__(self, fan, db):
        self.db_controller = db #DBController
        self.fan_controller = fan #FanController
        
        
        self.co2_limit = 1500
        self.co_limit = 10
        # self.pm1_limit = None # no use
        self.pm25_limit = 35
        self.pm10_limit = 100
        
        # safe range
        self.co2_safe = 700
        self.co_safe = 1
        self.pm25_safe = 20
        self.pm10_safe = 30
        
        self.send_db_interval = None
        self.send_app_interval = None
    
    
    def start(self):
        while True:
            try:
                co2_value = co2.read()['co2']
                co_value = co.read()
                pm_values = pm.read()
                
                if self.fan_controller.is_on():
                    print('is on')
                    if self.co2_safe >= co2_value \
                    and self.co_safe >= co_value \
                    and self.pm25_safe >= pm_values['pm2.5'] \
                    and self.pm10_safe >= pm_values['pm10']:
                        print('@ try off')
                        self.fan_controller.off()
                        pass
                    pass
                    
                else: # is off
                    print('is off')
                    if self.co2_limit <= co2_value \
                    or self.co_limit <= co_value \
                    or self.pm25_limit <= pm_values['pm2.5'] \
                    or self.pm10_limit <= pm_values['pm10']: 
                        print('@ try on')
                        self.fan_controller.on()
                        print('@@ try on end @@')
                        pass
                    pass
                
                            
                #test begin
                print('co2: {}'.format(co2_value))
                print('co: {}'.format(co_value))
                print('pm1.0: {}'.format(pm_values['pm1.0']))
                print('pm2.5: {}'.format(pm_values['pm2.5']))
                print('pm10: {}'.format(pm_values['pm10']))
                print('')
                #test end
                
                time.sleep(1)
                
            except:
                #do nothing
                pass
