import threading
import pymysql

class DBController:
    
    def __init__(self):
        # self.driver_address = None #String
        # self.ipv4_address = None #String
        self.id = 'admin' #String
        self.password = '1234' #String

        self.locker = threading.Lock()
        
        
    def connect(self):
        self.connector = pymysql.connect(host='127.0.0.1', user= self.id, \
             password = self.password, db='smart_vent', charset='utf8')
        self.cursor = self.connector.cursor()
        
    def disconnect(self):
        self.connector.commit()
        self.connector.close()
        self.connector=None
        self.cursor=None

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
    
    def insert_sensing(self, pm10, pm25, co, co2, log):
        self.locker.acquire()
        
        self.connect()
        
        query = 'INSERT INTO sensing VALUES(0, now(), {}, {}, {}, {}, "");'.format(pm10, pm25, co, co2, log)
        self.cursor.execute(query)
        
        self.connector.commit()
        
        self.locker.release()
        pass
    
    def get_today():
        self.locker.acquire()
        
        self.connect()
        query = 'select time, pm10, pm25, co, co2 from sensing where time>"{} 00:00:00"'.format(str(datetime.now().date()))
        
        cursor.execute(query)
        result = cursor.fetchall()
        self.locker.release()

        array = []

        for e in result:
            array.append({ 'time':e[0], 'pm10':e[1], 'pm25':e[2], 'co':e[3], 'co2':e[4]})
            
        return {'data' : array}
        