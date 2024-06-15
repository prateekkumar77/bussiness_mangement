from mysql import connector

MYSQL_ROOT_PASSWORD = 'root-pass'
MYSQL_USER = 'root'
DATABASE_NAME = 'Test_DB1'
HOST = 'localhost'


def get_live_db_object(logger):
    
    try:
        db = connector.connect(host=HOST,user=MYSQL_USER,password=MYSQL_ROOT_PASSWORD,database=DATABASE_NAME,)
    except (connector.Error, IOError) as err:
        #print("Failed to connect")
        logger.error("Failed to connect to database: %s", err.errno)
        return False

    logger.info("Connection to {DB: "+DATABASE_NAME+"} with {user: "+MYSQL_USER+"} Successful")
    #print('Connection Established')

    return db

#db1 = get_live_db_object()