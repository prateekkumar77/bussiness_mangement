import streamlit as st
from streamlit_searchbox import st_searchbox


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
  st.header("🧑‍💼 :orange[Member Data Manager]")
  st.markdown("")
  st.markdown("")
  st.markdown("")
  
  col1,col2 = st.columns(2)
  metric = col1.metric(label="Total Clients", value=totalClients, delta=change, help="Value in color represent the change in numbers in within a week")
  metric2 = col2.metric(label="Active Susbcriptions", value=activeSusbscription, delta=changeSusbcription)
  #st.metric(label="Total Clients", value=totalClients, delta=change, help="Value in color represent the change in numbers in within a week")

  #addClientBtn = st.button(label="Register", on_click=addClient)
  selected_item = st_searchbox(search_function=search, key="search-box",placeholder="Search All Clients")
  st.markdown("")
  st.markdown("")
  c1,c2,c3 = st.columns(3)
  button1 = c1.button(label="View", type="secondary",use_container_width=True)
  button2 = c2.button(label="Edit", type="secondary",use_container_width=True)
  button3 = c3.button(label="Delete", type="secondary",use_container_width=True)
  st.markdown("")
  st.markdown("")

  if button1:
     if selected_item == "" or selected_item is None:
        st.warning("Please select a member to take action",icon="🚫")
     else:
        st.success("Member Data Loaded")
     
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