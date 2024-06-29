import streamlit as st
from streamlit_searchbox import st_searchbox
from models import client
from features import initialize_logger

logger = initialize_logger(__name__)

clients = []
totalClients = 117 #len(clients)
change = 23
activeSusbscription = 0
changeSusbcription = 0

if change < 0:
  change = '-' + str(change)
else:
  change = "+" + str(change)


def search(item:str):
   return ["Test1", "Test2", "Test3", "test4"]

def app():
  st.header("🧑‍💼 :orange[Member Data Manager]",divider=True)
  st.markdown("")
  st.markdown("")
  st.markdown("")

  totalClients = client.get_total_count()
  activeSusbscription = client.get_subscribed_count()
  
  col1,col2 = st.columns(2)
  metric = col1.metric(label="Total Clients", value=totalClients, help="Value in color represent the change in numbers in within a week")
  metric2 = col2.metric(label="Active Susbcriptions", value=activeSusbscription)
  
  selected_item = st_searchbox(search_function=client.search_client, key="search-box",placeholder="Search All Clients")
  st.markdown("")
  st.markdown("")
  c1,c2,c3 = st.columns(3)
  flag = True
  if selected_item is not None and selected_item != "":
     st.success("{} member selected".format(selected_item.split(":")[0]))
     flag = False
  button1 = c1.button(label="View", type="secondary",use_container_width=True, disabled=flag)
  button2 = c2.button(label="Edit", type="secondary",use_container_width=True, disabled= flag)
  button3 = c3.button(label="Delete", type="secondary",use_container_width=True, disabled=flag)
  st.markdown("")
  st.markdown("")

  if button1:
     if selected_item != "" and selected_item is None:
        st.warning("Please select a member to take action",icon="🚫")
     else:
        cbs = selected_item.split(":")[2].lstrip().rstrip()
        print(cbs)
        mem = client.getClientInfo(cbs)[0]
        if mem is not None:
         st.json({'client_id': mem[0], 'name':mem[1], 'phone':mem[2], 'flat_no':mem[3], 'society':mem[4], 'address':mem[5]})
         st.success("Member Data Loaded")
        else:
           st.warning("Internal error occured")
           logger.warning("Member data cannot be fetched")
     
  if button2:
     if selected_item == "" or selected_item is None:
        st.warning("Please select a member to take action",icon="🚫")
     else:
        st.success("Member Data Modified")
  
  if button3:
     if selected_item == "" or selected_item is None:
        st.warning("Please select a member to take action",icon="🚫")
     else:
        st.success("Member Data Deleted")