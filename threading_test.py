import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


DISABLED = 0
NONE_FOUND = 1
NOTIFY = 2
ALARM = 3


new_state = NONE_FOUND
blink_rate = 0.5

class LEDController(threading.Thread):
    #def __init__(self, blink_rate, brightness):
    #    self.blink_rate = blink_rate
    #    self.brightness = brightness
    
    def run(self):
        logging.debug('Starting')
        prev_state = DISABLED
        while True:
            if prev_state != new_state:
                if prev_state == NONE_FOUND and new_state == DISABLED:
                    logging.debug('DISABLED1')
                    logging.debug("GREEN:  OFF")
                
                elif prev_state == DISABLED and new_state == NONE_FOUND:
                    logging.debug('NONE_FOUND1')
                    logging.debug("GREEN:  ON")
                
                elif prev_state == NONE_FOUND and new_state == NOTIFY:
                    logging.debug('NOTIFY1')
                    logging.debug("RED:  ON")
                
                elif prev_state == NOTIFY and new_state == NONE_FOUND:
                    logging.debug('NONE_FOUND2')
                    logging.debug("RED:  OFF")
                    
                elif prev_state == ALARM and new_state == NONE_FOUND:
                    logging.debug('NONE_FOUND3')
                    logging.debug("RED:  OFF")
                    
                elif prev_state == NONE_FOUND and new_state == ALARM:
                    logging.debug('ALARM1')
                    logging.debug("RED:  BLINK")

                elif prev_state == NOTIFY and new_state == ALARM:
                    logging.debug('ALARM2')
                    logging.debug("RED:  BLINK")
                    
                elif prev_state == ALARM and new_state == NOTIFY:
                    logging.debug('NOTIFY2')
                    logging.debug("RED:  ON")

                elif prev_state == ALARM and new_state == DISABLED:
                    logging.debug('DISABLED2')
                    logging.debug("GREEN:  OFF RED:  OFF")
                
                elif prev_state == NOTIFY and new_state == DISABLED:
                    logging.debug('DISABLED3')
                    logging.debug("GREEN:  OFF RED:  OFF")
            
                prev_state = new_state
                
                # turn on red leds
                # sleep(blink_rate)
                # turn off red leds
                # sleep(blink_rate)
                

thr = LEDController()
logging.debug('starting in main')
thr.setDaemon(True)
thr.start()
time.sleep(1)
new_state = NONE_FOUND
time.sleep(1)
new_state = NOTIFY
time.sleep(1)
new_state = ALARM
time.sleep(5)
new_state = DISABLED
time.sleep(1)
