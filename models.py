#data which is persisted in a database is defined here

class client:
    name:int
    phone:int
    address:str
    balance:int
    suscribed:bool
    emailID:str
    clientID:str


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

