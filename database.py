from mysql import connector
from features import initialize_logger
import json

sec_file = open('db_secrets.json')
data = json.load(sec_file)

MYSQL_ROOT_PASSWORD = data['pass']
MYSQL_USER = data['user']
DATABASE_NAME = data['database']
HOST = data['host']

logger = initialize_logger(__name__)


def get_live_db_object():
    
    try:
        db = connector.connect(host=HOST,user=MYSQL_USER,password=MYSQL_ROOT_PASSWORD,database=DATABASE_NAME,)
        logger.debug("Connection to {DB: "+DATABASE_NAME+"} with {user: "+MYSQL_USER+"} Successful")
    except connector.Error as err:
        logger.error(err)
        return False

    return db

#db1 = get_live_db_object()