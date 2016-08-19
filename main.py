import ConfigParser
import mysql.connector


def load_config_options(config_file, section):
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    return config.items(section)
    
def open_mysqldb(db_options):
    print type(db_options)
    return mysql.connector.connect(**db_options)
    



if __name__ == "__main__":
    CONFIG_FILE = "config\\config.ini"
    db_options = load_config_options(CONFIG_FILE, 'Database')
    cnx  = open_mysqldb(db_options)
    cursor = cnx.cursor()
    print cursor.fetchone()
    