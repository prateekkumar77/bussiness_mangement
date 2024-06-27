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
        #self.address1 = address1
        #self.flat_no = flat_no
        #self.society = society
        self.email_id = email_id
        self.phone_no = phn_no
        self.plan = plan
        self.balance = 0


    def delete_client(self, client_id:str) ->bool:
        sql = 'DELETE FROM clients WHERE client_id = "{}"'.format(client_id)

        db = get_live_db_object()
        if db is not False:
            cursor = db.cursor()

            try:
                logger1.debug("DELETE FROM clients; DB Query Executed")
                cursor.execute(sql)
                db.commit()
                logger1.debug(str(cursor.rowcount)+" record deleted from clients table")
            except mysql_error as err:
                logger1.error(err)
                return False
            cursor.close()
            db.close()
            logger1.debug("DB connection closed...")
        else:
            return False
        return True


    def save(self) ->bool:
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
                    logger1.debug(str(cursor.rowcount)+" record inserted into clients table")
                    cursor.close()
                    flag = True
                except mysql_error as err:
                    logger1.error(err)
                db.close()
                logger1.debug("DB connection closed...")
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

    def search_client(client_name:str) ->list:
        sql = 'select client_name, client_id, email_id from clients where client_name like "{}%";'.format(client_name)
        db = get_live_db_object()
        if db is not False:
            cursor = db.cursor()
            logger1.debug("SQL SELECT QUERY EXCECUTED")
            cursor.execute(sql)
            logger1.debug(str(cursor.rowcount)+" record(s) fetched")
            res = cursor.fetchall()
            #print(res)
            cursor.close()
            db.close()
            logger1.debug("DB connection closed...")
        ls = []
        for r in res:
            ls.append("{} : {} : {}".format(r[0],r[2],r[1]))
        return ls


    def getClientInfo(client_id:str) ->list|bool:
        #print("client_id :{}:".format(client_id))
        #sql = 'select client_name, client_id, email_id from clients where client_name like "{}%";'.format(client_id)
        sql = 'SELECT clients.client_id, clients.client_name, clients.phone_number, client_address1.flat_no, client_address1.society, client_address1.address FROM clients, client_address1 WHERE clients.client_id = client_address1.client_id AND clients.client_id = "{}";'.format(client_id)
        db = get_live_db_object()
        cursor = db.cursor()
        if db is not False:
            try:
                logger1.debug("SELECT FROM orders, clients; DB Query Executed")
                cursor.execute(sql)
                
            except mysql_error as err:
                logger1.error(err)
                return False
        
        res = cursor.fetchall()
        logger1.debug('{} row(s) fetched from DB'.format(len(res)))
        cursor.close()
        db.close()
        #print(res)
        return res

class orders:

    def __init__(self, client_id:str, amount:int, products:list[list[str]], date:str, time:str, inst:str, p_stat:str="U", d_stat:str="U", order_id:str="") -> None:
        self.orderID = order_id
        self.clientID = client_id
        self.payment_status = p_stat
        self.delivery_status = d_stat
        self.amount = amount
        self.products = products
        self.delivery_date = date
        self.instruction = inst
        self.delivery_time = time
        #self.date_created = str(datetime.date.today())

    def delete_order(order_id:str):
        sql ='DELETE FROM orders WHERE order_id = "{}";'.format(order_id)
        db = get_live_db_object()
        if db is False:
            return False
        cursor = db.cursor()

        try:
            logger1.debug("DELETE FROM orders; DB Query Executed")
            cursor.execute(sql)
            db.commit()
            logger1.debug("{} row deleted".format(cursor.rowcount))
            cursor.close()
            db.close()
            logger1.debug("DB Connection closed....")
            return True
        except mysql_error as err:
            logger1.error(err)
            cursor.close()
            db.close()
            logger1.debug("DB Connection closed....")
            return False

    def mark_delivery(status:str,order_id:str) ->bool:
        sql = 'UPDATE orders SET delivery_status = "{}" WHERE order_id = "{}";'.format(status,order_id)
        db = get_live_db_object()
        cursor = db.cursor()
        try:
            logger1.debug("UPDATE orders; DB Ouery Executed")
            cursor.execute(sql)
            db.commit()
            logger1.debug("{} row affected".format(cursor.rowcount))
        except mysql_error as err:
            logger1.error(err)
            return False
        cursor.close()
        db.close()
        logger1.debug("DB Connection Closed...")
        return True

    def mark_order(order_id:str,mark:str) ->bool:
        sql = 'UPDATE orders SET payment_status = "{}" WHERE order_id = "{}";'.format(mark, order_id)
        db = get_live_db_object()
        cursor = db.cursor()
        try:
            logger1.debug("UPDATE orders; DB Ouery Executed")
            cursor.execute(sql)
            db.commit()
            logger1.debug("{} row affected".format(cursor.rowcount))
        except mysql_error as err:
            logger1.error(err)
            return False
        cursor.close()
        db.close()
        logger1.debug("DB Connection Closed...")
        return True
    
    def getOrder_timeframe(order_date:str) :
        sql = 'SELECT orders.order_id, orders.client_id, clients.client_name, clients.phone_number, client_address1.flat_no, client_address1.society, client_address1.address, orders.delivery_time, orders.delivery_status, orders.payment_status FROM orders, clients, client_address1 WHERE orders.client_id = clients.client_id AND clients.client_id = client_address1.client_id AND orders.date_created LIKE "{}%";'.format(order_date)
        db = get_live_db_object()
        if db is False:
            return False
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            #print("res {}".format(res))
            logger1.debug("{} row(s) fetched".format(cursor.rowcount))
        except mysql_error as err:
            logger1.error(err)
            return False
        cols = ['Order ID', 'Client ID', 'Client Name', 'Phone Number', 'Flat No.', 'Society', 'Address', 'Delivery Time', 'Delivery Status' , 'Payment Status']
        #for r in res:
         #   r = list(r)
          #  r[7] = str(r[7])
        #print(res)
        cursor.close()
        db.close()
        return res, cols
    
    def getOrder_timeframe2(order_date:str) :
        sql = 'SELECT orders.order_id, orders.client_id, clients.client_name, clients.phone_number, client_address1.flat_no, client_address1.society, client_address1.address, orders.delivery_time, orders.delivery_status, orders.payment_status FROM orders, clients, client_address1 WHERE orders.client_id = clients.client_id AND clients.client_id = client_address1.client_id AND orders.delivery_date = "{}";'.format(order_date)
        db = get_live_db_object()
        if db is False:
            return False
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            #print("res {}".format(res))
            logger1.debug("{} row(s) fetched".format(cursor.rowcount))
        except mysql_error as err:
            logger1.error(err)
            return False
        cols = ['Order ID', 'Client ID', 'Client Name', 'Phone Number', 'Flat No.', 'Society', 'Address', 'Delivery Time', 'Delivery Status' , 'Payment Status']
        #for r in res:
         #   r = list(r)
          #  r[7] = str(r[7])
        #print(res)
        cursor.close()
        db.close()
        return res, cols
    
    def getOrders_cID(client_id:str) ->list|bool:
        sql = 'SELECT orders.order_id, clients.client_id, orders.date_created, orders.amount, orders.payment_status, orders.delivery_status, clients.email_id FROM orders, clients WHERE orders.client_id = clients.client_id AND orders.client_id = "{}";'.format(client_id)

        db = get_live_db_object()
        cursor = db.cursor()

        try:
            logger1.debug("SELECT FROM orders, clients; DB Query Executed")
            cursor.execute(sql)
            logger1.debug('{} row(s) fetched from DB'.format(cursor.rowcount))
        except mysql_error as err:
            logger1.error(err)
            return False
        
        res = cursor.fetchall()
        cursor.close()
        db.close()
        column_name = ['Order ID', 'Client ID', 'Order Date', 'Amount', 'Payment Status', 'Delivery Status', 'Email ID']

        logger1.debug("DB connection closed...")
        return res, column_name


    def save(self) -> bool:
        flag = False
        self.orderID = "OD" + str(random.randint(100001,999999))
        prod_dict = {"DEJ01":0, "DEJ02":0, "DEJ03":0, "DEJ04":0, "DEJ05":0, "DEJ06":0,}
        if len(self.products) > 0:
            for prd in self.products:
                prod_dict[prd[0]] += prd[1]
        else:
            logger1.warning("Products are not assigned to orders objects. Can't push data with blank values.")
            return False

        sql = 'INSERT INTO orders (order_id, client_id, amount, dej01, dej02, dej03, dej04, dej05, dej06, delivery_date, instruction, delivery_time ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (self.orderID, self.clientID, self.amount, prod_dict["DEJ01"], prod_dict["DEJ02"], prod_dict["DEJ03"], prod_dict["DEJ04"], prod_dict["DEJ05"], prod_dict["DEJ06"], self.delivery_date, self.instruction, self.delivery_time)

        db = get_live_db_object()
        if db is not False:
            cursor = db.cursor()
            try:
                logger1.debug("INSERT INTO orders; DB Query Executed.")
                cursor.execute(sql,val)
                db.commit()
                logger1.debug("{} record inserted into orders table".format(cursor.rowcount))
                flag = True
            except mysql_error as err:
                logger1.error(err)
            cursor.close()
            db.close()
            logger1.debug("DB connection closed...")
            return flag
        else:
            logger1.warning("Unable to connect to database.")
            return False



    def select_products(self, product_codes:list) ->None:
        self.products = product_codes


    def save1(self) ->bool:
        flag = False
        db = get_live_db_object()
        if db is not False:
            cursor = db.cursor()
            sql = "INSERT INTO orders (order_id, client_id, address_id, products) VALUES (%s, %s, %s, %s)"
            val = (self.orderID, self.clientID, self.addID, self.products)
            logger1.debug("INSERT INTO orders; DB Query Executed")
            try:
                cursor.execute(sql,val)
                db.commit()
                logger1.debug(str(cursor.rowcount) + " record inserted into orders table")
                flag = True
            except mysql_error as err:
                logger1.err(err)
            cursor.close()
            db.close()
            logger1.debug("DB connection closed...")
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
                logger1.debug("INSERT INTO client_address;  DB Query Executed")
                cursor.execute(sql,val)
                db.commit()
                logger1.debug(str(cursor.rowcount)+" row inserted into client_address1 table")
                flag = True
            except mysql_error as err:
                logger1.debug(err)
            cursor.close()
            db.close()
            logger1.debug("DB connection closed...")
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
             logger1.debug("INSERT INTO products; DB Query Executed")
             cursor.execute(sql, val)
             db.commit()
             logger1.debug(str(cursor.rowcount) + " record inserted into produts table")
             flag = True
        except mysql_error as err:
             logger1.error(err)
             print(err)
            
        cursor.close()
        db.close()
        logger1.debug("DB connection closed...")
        return flag
    
    def getAllProducts() ->list:

        db = get_live_db_object()

        if db is False:
            return [-1]
        
        cursor = db.cursor()
        logger1.debug("SELECT FROM products; DB Query Executed")
        try:
            cursor.execute("SELECT p_id, product_name, category, price FROM products")
        except mysql_error as err:
            logger1.error(err)
            db.close()
            logger1.debug("DB connection closed...")
            return [-2]
        
        res = cursor.fetchall()
        logger1.debug(str(cursor.rowcount)+" row(s) fetched from products table")
        cursor.close()
        db.close()
        logger1.debug("DB connection closed...")
        return res


class subscription_plans:
    subscriptionID:str
    products:list[str]
    validity:int
    susbscriptions_desc:str
    default_delivery_time:str
    price:int