import streamlit as st
from features import reset, getProductList
from models import client
from streamlit_searchbox import st_searchbox
import datetime

cart = 0


def search(item:str):
   return ["Test1", "Test2", "Test3", "test4"]

def app():
  global cart


## Order Page UI

  st1 = "IN 🧺 Cart {} item(s) ".format(str(cart))
  st.header("🥡 :orange[Orders Manager] ",divider=True)

  st.markdown("<h2>"+st1+"<h2>",unsafe_allow_html=True)

  products = getProductList()
  no_products = len(products)
  reqRows = no_products // 4

  if no_products % 4 !=0:
    reqRows = (no_products // 4) + 1
  
  rows = []

# Menu GRID UI 
  expan1 = st.expander("Category 1")

  con1 = expan1.container()
  k = 0
  for r in range(reqRows):
    col = con1.columns(4)
    for c in range(4):
      if k >= no_products:
        break
      key1 = "p" + str(k)
      key2 = "q" + str(k)
      col[c].text(products[k])
      
      c1 = col[c].checkbox("Add to Cart",key=key1,)
      q1 = col[c].number_input(label="Quantity", max_value=5,min_value=1,value=1,key=key2)
      rows.append([c1,q1,products[k]])
      k += 1

#Client Form UI
  
  client_check = st.checkbox(label="For Existing Member", key="check1")

  client1 = client()

  if client_check:
    sb_value = st_searchbox(search_function=search, key="sb2", clear_on_submit=True, placeholder="Search All Clients")
    if sb_value:
      st.success("Selected Member: {}".format(sb_value))
    else:
      st.warning("Please Select a Member")
    #print("Selected value {}".format(sb_value))
    con_client = st.container()
  
  else:
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

  ins = con_client.text_input(label="Special Instructions", key="ins1", max_chars=50)
  delivery_time = con_client.time_input(label="Select a delivery Time", value=datetime.time(hour=6,minute=30), help="Time is in IST Timezone")
  del_date = ""
  cbx3 = con_client.checkbox("Delivery Not Today", key="date_cb")
  if cbx3:
    del_date = con_client.date_input("Choose a Date",value="today",min_value=datetime.date.today())




#Cart Value Calculation
  p = 0
  x = False

  for r in range(no_products):
    if rows[r][0]:
      p += rows[r][1]
    if x is False and rows[r][0] is True:
      x = True
  

  if not x:
    p = 0
  
  if cart != p:
    cart = p
    st.rerun()


#Reset Button
  col1,col2,col3 = st.columns(3)
  button1 = col1.button("Reset", key='reset', on_click=reset)
  button2 = col2.button("Order", key='order')

