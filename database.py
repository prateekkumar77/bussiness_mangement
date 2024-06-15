from mysql import connector
from features import log_info, log_error

i_log = log_info(__name__)
err_log = log_error(__name__)

MYSQL_ROOT_PASSWORD = 'root-pass'
MYSQL_USER = 'root'
DATABASE_NAME = 'Test_DB1'
HOST = 'localhost'



def get_live_db_object() -> connector.connect:
    try:
        db = connector.connect(host=HOST,user=MYSQL_USER,password=MYSQL_ROOT_PASSWORD,database=DATABASE_NAME,)
    except (connector.Error, IOError) as err:
        print("Failed to connect")
        print(err)
        err_log.error("Failed to connect to database: %s", err.errno)

    i_log.info("Connected to database: "+DATABASE_NAME+" with user: "+MYSQL_USER)
    print('Connection Established')

    return db

#db1 = get_live_db_object()