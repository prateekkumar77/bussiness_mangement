#data which is persisted in a database is defined here
import datetime, random
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
                cursor = db.cursor()
                sql = "INSERT INTO clients (email_id, client_name, client_id, phone_number, subscribed, end_date, balance) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (self.email_id, self.name, self.client_id, self.phone_no, self.subscribed, self.end_date, self.balance)
                try:
                    logger1.info("INSERT INTO clients; DB Query Excuted")
                    cursor.execute(sql,val)
                    db.commit()
                    logger1.info(str(cursor.rowcount)+" record inserted into clients table")
                    cursor.close()
                    flag = True
                except mysql_error as err:
                    logger1.error(err)
                db.close()
                logger1.info("DB connection closed...")
        else:
            logger1.warning("save() function is called but values are not assigned")
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

    def __init__(self, order_id:str, client_id:str, add_id:str, amount:int) -> None:
        self.orderID = order_id
        self.clientID = client_id
        self.addID = add_id
        #self.products = products
        self.amount = amount
        self.products = []


    def select_products(self, product_codes:list) ->None:
        self.products = product_codes


    def save(self) ->bool:
        flag = False
        db = get_live_db_object()
        if db is not False:
            cursor = db.cursor()
            sql = "INSERT INTO orders (order_id, client_id, address_id, products) VALUES (%s, %s, %s, %s)"
            val = (self.orderID, self.clientID, self.addID, self.products)
            logger1.info("INSERT INTO orders; DB Query Executed")
            try:
                cursor.execute(sql,val)
                db.commit()
                logger1.info(str(cursor.rowcount) + " record inserted into orders table")
                flag = True
            except mysql_error as err:
                logger1.err(err)
            cursor.close()
            db.close()
            logger1.info("DB connection closed...")
        return flag
    

class address:
    def __init__(self, client_id:str, address_type:str, flat_no:str, society:str, address:str, address_id:str="") -> None:
        self.addressID = address_id
        self.client_id = client_id
        self.address_type = address_type
        self.flat_no = flat_no
        self.society = society
        self.address = address

    def save(self) ->(bool|str):
        flag = False
        if self.addressID == "":
            self.addressID = "AD" + str(random.randint(10001, 99999))
        db = get_live_db_object()

        if db is not False:
            cursor = db.cursor()
            sql = "INSERT INTO client_address1 (address_id, client_id, address_type, flat_no, society, address) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (self.addressID, self.client_id, self.address_type, self.flat_no, self.society, self.address)
            try:
                logger1.info("INSERT INTO client_address;  DB Query Executed")
                cursor.execute(sql,val)
                db.commit()
                logger1.info(str(cursor.rowcount)+" row inserted into client_address1 table")
                flag = True
            except mysql_error as err:
                logger1.error(err)
            cursor.close()
            db.close()
            logger1.info("DB connection closed...")
        if flag:
            return self.addressID
        else:
            return flag


class product:
    def __init__(self,id:str,name:str,description:str,price:int,img_url:str,category:str) -> None:
        self.p_id = id
        self.product_name = name
        self.description = description
        self.price = price
        #self.img_url = img_url
        self.category = category

    def add_product_toDB(self) -> bool:
        flag = False
        db = get_live_db_object(logger1)
        cursor = db.cursor()
        sql = "INSERT INTO products (p_id, product_name, product_description, price, category) VALUES (%s, %s, %s, %s, %s)"
        val = (self.p_id, self.product_name, self.description, self.price, self.category)
       
        try:
             logger1.info("INSERT INTO products; DB Query Executed")
             cursor.execute(sql, val)
             db.commit()
             logger1.info(str(cursor.rowcount) + " record inserted into produts table")
             flag = True
        except mysql_error as err:
             logger1.error(err)
             print(err)
            
        cursor.close()
        db.close()
        logger1.info("DB connection closed...")
        return flag
    
    def getAllProducts() ->list:

        db = get_live_db_object()

        if db is False:
            return [-1]
        
        cursor = db.cursor()
        logger1.info("SELECT FROM products; DB Query Executed")
        try:
            cursor.execute("SELECT p_id, product_name, category FROM products")
        except mysql_error as err:
            logger1.error(err)
            db.close()
            logger1.info("DB connection closed...")
            return [-1]
        
        res = cursor.fetchall()
        logger1.info(str(cursor.rowcount)+" row(s) fetched from products table")
        cursor.close()
        db.close()
        logger1.info("DB connection closed...")
        return res


class subscription_plans:
    subscriptionID:str
    products:list[str]
    validity:int
    susbscriptions_desc:str
    default_delivery_time:str
    price:int