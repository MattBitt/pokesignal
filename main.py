import ConfigParser
import mysql.connector
from datetime import datetime
from pytz import timezone


def load_config_options(config_file, section):
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    return dict(config.items(section))
    
def open_mysqldb(db_options):
    return mysql.connector.connect(**db_options)
    
def get_current_pokemon(cnx):

    current_time = datetime.now(timezone('UTC'))
    query_string = """SELECT * FROM pokemon WHERE disappear_time >  '{}' ORDER BY disappear_time""".format(current_time)
    cursor = cnx.cursor()
    cursor.execute(query_string)
    return cursor.fetchall()

def get_notify_pokemon(cnx):
    query_string = """SELECT pokemon_id FROM notify_pokemon"""
    cursor = cnx.cursor()
    cursor.execute(query_string)
    results = [item[0] for item in cursor.fetchall()]
    print "Notify:  "
    print results
    return results

def get_alarm_pokemon(cnx):
    query_string = """SELECT pokemon_id FROM alarm_pokemon"""
    cursor = cnx.cursor()
    cursor.execute(query_string)
    results = [item[0] for item in cursor.fetchall()]
    print "Alarm:  "
    print results
    return results
    
if __name__ == "__main__":
    CONFIG_FILE = "config/config.ini"
    db_options = load_config_options(CONFIG_FILE, 'Database')
    cnx  = open_mysqldb(db_options)
    current_pokemon = get_current_pokemon(cnx)
    # check distance here or in mysql query???
    available_pokemon = set()
    for pk in current_pokemon:
        available_pokemon.add(pk[2])
    
    print "total:  ", len(current_pokemon)
    notify_pokemon = get_notify_pokemon(cnx)
    alarm_pokemon = get_alarm_pokemon(cnx)
    print "available"
    print available_pokemon
    for pkmon in available_pokemon:
        if pkmon in notify_pokemon:
            print "NOTIFY", pkmon
        elif pkmon in alarm_pokemon:
            print "ALARM!!!", pkmon
            break  

            
