#data which is persisted in a database is defined here
import datetime

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
    productID:str
    productName:str
    price:int
    productImg:str


class subscription_plans:
    subscriptionID:str
    products:list[str]
    validity:int
    susbscriptions_desc:str
    default_delivery_time:str
    price:int


