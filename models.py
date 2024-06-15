#data which is persisted in a database is defined here
import datetime
from database import get_live_db_object
from mysql.connector import Error as mysql_error


class client:

    def __init__(self,name:str="",client_id:str=None,subscribed:bool=False,end_date:datetime=None,flat_no:str="",society:str="",address1:str="",email_id:str="",phn_no:int=None, plan:str="") -> None:
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


    def save(self):
        pass


    def assign_values(self,name,client_id,subscribed,end_date,flat_no,society,phn_no,email_id,plan=None,address1=""):
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

    def search_and_populate(self, client_name:str="", client_id:str=None):
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
        self.img_url = img_url
        self.category = category

    def add_product_toDB(self,logger1) -> bool:
        flag = True
        db = get_live_db_object(logger1)
        cursor = db.cursor()
        sql = "INSERT INTO products (p_id, product_name, product_description, price, image_url, category) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.p_id, self.product_name, self.description, self.price, self.img_url, self.category)
       
        try:
             logger1.info("DB INSERT query executed")
             cursor.execute(sql, val)
        except mysql_error as err:
             logger1.error(err)
             print(err)
             flag = False
        
        if flag:
            print(cursor.rowcount, " record inserted.")
            db.commit()
            logger1.info(str(cursor.rowcount) + " record inserted")
        cursor.close()
        db.close()
        return flag



class subscription_plans:
    subscriptionID:str
    products:list[str]
    validity:int
    susbscriptions_desc:str
    default_delivery_time:str
    price:int


