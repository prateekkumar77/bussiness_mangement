import streamlit as st
from features import reset, initialize_logger
from models import client, product, orders
from streamlit_searchbox import st_searchbox
import datetime


cart = 0

def search(item:str):
   return ["Test1", "Test2", "Test3", "test4"]

logger = initialize_logger(__name__)

def app():
  global cart


## Order Page UI

  st1 = "IN 🧺 Cart {} item(s) ".format(str(cart))
  st.header("🥡 :orange[New Order Manager] ",divider=True)

  st.markdown("<h2>"+st1+"<h2>",unsafe_allow_html=True)

  products = product.getAllProducts()
  if products == [-1]:
    logger.error("Unable to connect to Database")

  dc = {}
  for prd in products:

    if prd[2] not in dc:
      dc[prd[2]] = [(prd[0],prd[1],prd[3])]
    else:
      dc[prd[2]].append((prd[0],prd[1],prd[3]))

  
  rows = []
  k = 0
  sb_value = st_searchbox(label="Search Client", search_function=client.search_client, key="sb2", placeholder="Search All Clients")
  #print("Value {}".format(sb_value))
  if sb_value is not None:
    st.success("Selected Member: {}".format(str(sb_value).split(":")[0]))
# Menu GRID UI 

  for category in dc:
    prds = dc[category]
    no_products = len(prds)
    reqRows = no_products // 4

    if no_products % 4 !=0:
      reqRows = (no_products // 4) + 1

    expan1 = st.expander(category)

    con1 = expan1.container()
    
    for r in range(reqRows):
      col = con1.columns(4)
      for c in range(4):
        if k >= no_products:
          break
        key1 = "p" + str(k)
        key2 = "q" + str(k)
        col[c].text(prds[k][1])
        
        c1 = col[c].checkbox("Add to Cart",key=key1,on_change=None)
        q1 = col[c].number_input(label="Quantity", max_value=5,min_value=1,value=1,key=key2)
        rows.append([c1,q1,prds[k][0],prds[k][2]])
        k += 1

#Client Form UI
  
  client_check = st.checkbox(label="For Existing Member", key="check1")

  selected_member = ""
  if client_check:
    selected_member = sb_value
    #print(sb_value)
    
    if sb_value:
      #st.success("Selected Member: {}".format(sb_value))
      pass
    else:
      st.warning("Please Select a Member")
    #print("Selected value {}".format(sb_value))
    con_client = st.container()
  
  else:
    client1 = client()
    con_client = st.container()
    col1,col2 = con_client.columns(2)
    client_name1 = col1.text_input(label="First Name", key="cl-fname", placeholder="Enter First Name",max_chars=15)
    client_name2 = col2.text_input(label="Last Name", key="cl-lname", placeholder="Enter Last Name",max_chars=15)
    phno = con_client.text_input(label="Phone Number", key="phn_no",max_chars=10, placeholder="9XX-XXXX-XX9")
    add_exp = con_client.expander(label="Enter Address")
    add_con = add_exp.container()
    col3,col4 = add_con.columns(2)
    add_flat_no = col3.text_input(label="Flat No.", max_chars=5, key="cl-flat", placeholder="Flat/Apartment No.")
    add_society = col4.text_input(label="Society", max_chars=20, key="cl-society", placeholder="Society Name")
    add_remainder = add_con.text_input(label="Address Line 2", max_chars=50, key='cl-address', placeholder="Address Line 2")

  ins = con_client.text_area(label="Special Instructions", key="ins1", max_chars=50)
  delivery_time = con_client.time_input(label="Select a delivery Time", value=datetime.time(hour=6,minute=30), help="Time is in IST Timezone")
  del_date = datetime.date.today()
  cbx3 = con_client.checkbox("Delivery Not Today", key="date_cb")
  if cbx3:
    del_date = con_client.date_input("Choose a Date",value="today",min_value=datetime.date.today())


#Cart Value Calculation
  p = 0
  x = False
  amount = 0
  
  #print(rows)
  p_list = []
  for r1s in rows:
    #print(r1s)
    if r1s[0]:
      p += r1s[1]
      #print("{} {} {}".format(rows[1],rows[3],rows[]))
      amount += (r1s[1]*r1s[3])
      p_list.append([r1s[2],r1s[1]])
  #print(amount)
  #if cart != p:
   # cart = p
    #st.rerun()


#Reset Button
  col1,col2 = st.columns(2)
  button1 = col1.button("Reset", key='reset', on_click=reset,use_container_width=True)
  button2 = col2.button("Order", key='order',use_container_width=True)

  if button2:
    if p == 0:
      st.warning("Please select alteast 1 product to place an Order")
    else:
      
      #for ps in rows:
       # p_list.append([ps[2],ps[1]])
      print(p_list)
      if selected_member == "" or selected_member is None:
        logger.warning("Member not selected before placing the order")
        st.warning("Please select a member to place order")
      else: 
        od1 = orders(client_id=str(sb_value).split(":")[2].lstrip(), amount=amount,products=p_list,date=str(del_date),time=str(delivery_time),inst=ins)

        if od1.save():
          logger.info("New order created Order_ID: {}".format(od1.orderID))
          st.success("Order Created. OrderID: {}".format(od1.orderID))
        else:
          logger.warning("Order Failed. Switch to Debug logs for more info")
          st.warning("Order Failed. Please Try Again")

