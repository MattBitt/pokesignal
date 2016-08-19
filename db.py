import sqlite3
from datetime import datetime


notify = [1,4,7,25,37,58,74,75,77,79,81,93,96,100,104]
alarm = [2,3,5,6,8,9,26,35,36,38,40,45,53,57,
              59,62,63,64,65,66,67,68,76,80,82,83,85,86,
              87,89,90,91,94,95,97,101,105,106,107,113,115,
              124,125,126,130,131,132,137,138,139,140,141,
              142,143,144,145,146,147,148,149,150,151]

DISABLED = 0
NONE_FOUND = 1
NOTIFY = 2
ALARM = 3
              
state = 1


conn = sqlite3.connect('pogom.db')

c = conn.cursor()
current_time = datetime.now()
query_string = """SELECT * FROM pokemon WHERE disappear_time >  '{}'""".format(str(current_time))
query_string = """SELECT * FROM pokemon WHERE disappear_time >  '{}' ORDER BY disappear_time""".format("2016-06-01")
print query_string
results = c.execute(query_string)
available_pokemon = []
for row in results:
    available_pokemon.append(row[2])
    
available_pokemon = set(available_pokemon)
for p in notify:
    if p in available_pokemon:
        state = NOTIFY
        print "Notify {}".format(p)

for p in alarm:
    if p in available_pokemon:
        state = ALARM
        print "Alarm {}".format(p)

print state
    #dt = results.fetchone()[5]
#print dt
#print type(dt)
#record_time = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S.%f")

#time_diff = current_time - record_time
#print time_diff.seconds
def delta_time(despawn_time):
    despawn_time = datetime.strptime(despawn_time, "%Y-%m-%d %H:%M:%S.%f")
    
