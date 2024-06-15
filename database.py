from mysql import connector
from mysql.connector import errorcode
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Log to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Also log to a file
file_handler = logging.FileHandler("app-info.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

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
        logger.error("Failed to connect to database: %s", err.errno)

    logger.info("Connected to database: "+DATABASE_NAME+" with user: "+MYSQL_USER)
    print('Connection Established')

    return db

db1 = get_live_db_object()

cur = db1.cursor()

sql = "INSERT INTO products (p_id, product_name, product_description, price, image_url, category) VALUES (%s, %s, %s, %s, %s, %s)"
val = ('self.p', 'self.product_name', 'self.description', 500, 'self.img_url', 'self.category')

flag = True
try:
    cur.execute(sql, val)
except connector.Error as err:
       print(err)
       flag = False

if flag:
    print(cur.rowcount, "record inserted.")
    #i_log.info(str(cur.rowcount) + " record inserted")
    #db1.commit()
    cur.close()
    db1.commit()
    db1.close()