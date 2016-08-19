# store these tables in the pokemongo db
notify = [1,4,7,25,37,58,74,75,77,79,81,93,96,100,104]
alarm = [2,3,5,6,8,9,26,35,36,38,40,45,53,57,
              59,62,63,64,65,66,67,68,76,80,82,83,85,86,
              87,89,90,91,94,95,97,101,105,106,107,113,115,
              124,125,126,130,131,132,137,138,139,140,141,
              142,143,144,145,146,147,148,149,150,151]
              
class LEDController(threading.Thread):
    def __init__(self, blink_rate, brightness):
        self.blink_rate = blink_rate
        self.brightness = brightness
    
    def run(self):
        while True:
            if state == DISABLED:
                # turn off red & green leds
            else:
                # turn on green led
            
            if state == NONE_FOUND:
                # turn off red leds
                pass
            elif state == NOTIFY:
                # turn on red leds
                pass
            elif state == ALARM:
                # turn on red leds
                # sleep(blink_rate)
                # turn off red leds
                # sleep(blink_rate)
        
              
              
if __name__ == "__main__":
    db_config = {
                'user' : 'root', 
                'pass' : 'asdf', 
                'host' : '192.168.0.201', 
                'port' : 3306,
                'database' : 'pokemongo'
            }
    conn = open_mysqldb(**db_config)
    #create  ledcontroller thread (need to make sure to kill it when program stops)
    d = threading.Thread(name='daemon', target=LEDController)
	d.setDaemon(True)
    state = NONE_FOUND
    d.setDaemon(.5, 100)
    while True:
        if disabled_switch:
            state = DISABLED
            sleep(1)
        else:
            rows = GetAvaliablePokemon(conn) # disappear time > now
            #need error check here or in query function??
            available_pokemon = set()
            for row in rows:
                lat = row[3]
                lon = row[4]
                pokemon_id = row[2]
                if distance(home, (lat, lon)) < 2:
                    available_pokemon.add(pokemon_id)
            state = NONE_FOUND # might not be able to do this (depending on threading response??)
            for p in pokemon_notify():  #function should load pokemon_notify from mysql table
                if p in available_pokemon:
                    state = NOTIFY
                    break
            for p in pokemon_alarm():  # same as notify function
                if p in available_pokemon:
                    state = ALARM
                    break
            sleep(15)  # shouldn't use sleep here (blocks process)

    
# example from shazsterblog.blogspot.compile
# import RPi.GPIO as GPIO 
# import time 
# import threading

# GPIO.setmode(GPIO.BOARD) 
# GPIO.setup(7, GPIO.OUT) 

# class Blinker(threading.Thread):
    # def __init__(self, speed, times):    
        # threading.Thread.__init__(self);
        # self.speed = speed;    
        # self.times = times;

    # def run(self):
        # for i in range(0,self.times):
            # print "Time : %d" % ((i+1))
            # GPIO.output(7,True)
            # time.sleep(self.speed)
            # GPIO.output(7,False)
            # time.sleep(self.speed)
        # print "Blinking Complete!" 
        # GPIO.cleanup()    

# blinker = Blinker(1, 10)
# blinker.start()    