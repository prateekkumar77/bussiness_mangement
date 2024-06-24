import streamlit as st, datetime
from streamlit_searchbox import st_searchbox
from models import client, orders
from pandas import DataFrame

def call1():
    global s1
    s1 = False

    return 'rerun'

s1 = False

def app():
    global s1
    st.header(" :orange[Manage Orders]",divider="gray")

    #col1,col2 = st.columns(2)
    con1 = st.container()
    cb1 = con1.radio(label='Search Filter', options=['No Selection', 'Find by Time', 'Find by Client'], key='rd1', horizontal=True)
    val = None
    time = None
    if cb1 == 'Find by Time':
        
        col1,col2 = con1.columns(2)
        b1 = col1.radio(label="Select", key='r3', options=['Today', 'Yesterday', 'Custom'])
        
        time = b1
        if b1 == 'Custom':
            d1 = col2.date_input(label="Choose Date", key='date1')
            time = d1
        

    if cb1 == 'Find by Client':
        val = st_searchbox(label="Search Client", search_function=client.search_client, key="sb3", placeholder="Search All Clients")
    
    if val is not None and val != "None":
        time = None
        st.success("Selected Member : {}".format(val.split(":")[0]))
        pass

    if time is not None:
        if time == 'Today':
            time = str(datetime.date.today())
        elif time == 'Yesterday':
            time = str(datetime.date.today() - datetime.timedelta(1))
        else:
            time = str(time)
            
    #x1,x2,x3 = st.columns(3)
    #b3 = x2.button(label="Search", key='b3', use_container_width=True)
    con2 = st.container()
    x = ""
    if val is not None and val != "None":
        ods, col_names = orders.getOrders_cID(val.split(":")[2].lstrip().rstrip())
        df = DataFrame(data=ods, columns=col_names)
        x = con2.dataframe(data=df, use_container_width=True, on_select='rerun' ,selection_mode='single-row')
        #st.success(str(x))
        sel1 = x["selection"]['rows']
        if sel1 != []:
            st.success("Order {} selected".format(ods[sel1[0]][0]))