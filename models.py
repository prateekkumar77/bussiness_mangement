#data which is persisted in a database is defined here
import datetime
from database import get_live_db_object
from mysql.connector import Error as mysql_error
from features import initialize_logger

logger1 = initialize_logger(__name__)


class client:

    def __init__(self,name:str="",client_id:str=None,subscribed:str="",end_date:datetime=None,flat_no:str="",society:str="",address1:str="",email_id:str="",phn_no:int=None, plan:str="None") -> None:
        self.name = name
        self.client_id = client_id
        self.subscribed = subscribed
        self.end_date = end_date
        self.address1 = address1
        self.flat_no = flat_no
        self.society = society
        self.email_id = email_id
        self.phone_no = phn_no
        self.plan = plan
        self.balance = 0


    def save(self):
        flag = False
        
        if self.client_id is not None and self.name != "":
            db = get_live_db_object()
            if db is not False:
                flag = True
                cursor = db.cursor()
                sql = "INSERT INTO clients (email_id, client_name, client_id, phone_number, subscribed, end_date, balance) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (self.email_id, self.name, self.client_id, self.phone_no, self.subscribed, self.end_date, self.balance)
                logger1.info("SQL INSERT Query Excuted")
                try:
                    cursor.execute(sql,val)
                    logger1.info(cursor.rowcount()+" record inserted into clients table")
                    cursor.close()
                    
                except mysql_error as err:
                    logger1.error(err)
                    flag = False
            db.close()
            logger1.info("DB Disconnected")
        else:
            logger1.warning("Assign values to the object fisrt and then call save()")
        return flag
            


    def assign_values(self,name,client_id,subscribed,flat_no,society,phn_no,email_id,end_date="N/A",plan="None",address1=""):
        self.name = name
        self.client_id = client_id
        self.subscribed = subscribed
        self.end_date = end_date
        self.address1 = address1
        self.flat_no = flat_no
        self.society = society
        self.email_id = email_id
        self.phone_no = phn_no
        self.plan = plan

    def search_and_populate(self, client_name:str="", client_id:str=None) ->bool:
        pass

    def getClientInfo(self) ->dict|None:
        if self.client_id is not None:
            return {}
        else:
            return None
    

class order:
    orderID:str
    clientID:str
    itemcode:list[(str,int)]
    totalQuantity:int
    deliveryAddress:str
    deliveryTime:str
    discount:int
    total:int


class product:
    def __init__(self,id:str,name:str,description:str,price:int,img_url:str,category:str) -> None:
        self.p_id = id
        self.product_name = name
        self.description = description
        self.price = price
        #self.img_url = img_url
        self.category = category

    def add_product_toDB(self) -> bool:
        flag = True
        db = get_live_db_object(logger1)
        cursor = db.cursor()
        sql = "INSERT INTO products (p_id, product_name, product_description, price, category) VALUES (%s, %s, %s, %s, %s)"
        val = (self.p_id, self.product_name, self.description, self.price, self.category)
       
        try:
             logger1.info("DB INSERT query executed")
             cursor.execute(sql, val)
        except mysql_error as err:
             logger1.error(err)
             print(err)
             flag = False
        
        if flag:
            #print(cursor.rowcount, " record inserted.")
            db.commit()
            logger1.info(str(cursor.rowcount) + " record inserted")
        cursor.close()
        db.close()
        return flag
    
    def getAllProducts() ->list:

        db = get_live_db_object()

        if db is False:
            return [-1]
        
        cursor = db.cursor()
        logger1.info("DB SELECT query executed")
        cursor.execute("SELECT p_id, product_name, category FROM products")
        logger1.info("DB Query execution succuessful")
        res = cursor.fetchall()
        cursor.close()
        db.close()
        logger1.info("DB Disconnected")
        return res





class subscription_plans:
    subscriptionID:str
    products:list[str]
    validity:int
    susbscriptions_desc:str
    default_delivery_time:str
    price:int


