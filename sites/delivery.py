import streamlit as st
import datetime
from streamlit_searchbox import st_searchbox
from models import client
from pandas import DataFrame
from models import orders
import time as tf

def app():
    st.header("🛵 :orange[Manage Delivery]",divider='gray')
    #st.markdown("<h1 style= 'text-align: center'>Manage Deliveries<h1>", unsafe_allow_html=True)

    con1 = st.container()
    cb1 = con1.radio(label='Search Filter', options=['No Selection', 'Find by TimeFrame', 'Find by Client'], key='rd1', horizontal=True)
    val = None
    timeframe = None
    if cb1 == 'Find by TimeFrame':
        
        col1,col2 = con1.columns(2)
        b1 = col1.radio(label="Select", key='r3', options=['Today', 'Yesterday', 'Custom'])
        
        timeframe = b1
        if b1 == 'Custom':
            d1 = col2.date_input(label="Choose Date", key='date1')
            timeframe = d1
        

    if cb1 == 'Find by Client':
        val = st_searchbox(label="Search Client", search_function=client.search_client, key="sb4", placeholder="Search All Clients")
    
    con2 = st.container()
    con3 = st.container()
    if val is not None and val != "None":
        timeframe = None
        st.success("Selected Member : {}".format(val.split(":")[0]))
        pass

    sel1 = []
    mem = []
    if timeframe is not None:
        val = None
        if timeframe == 'Today':
            timeframe = str(datetime.date.today())
        elif timeframe == 'Yesterday':
            timeframe = str(datetime.date.today() - datetime.timedelta(1))
        else:
            timeframe = str(timeframe)

        cc1,cc2 = con2.columns(2)
        rb2 = cc1.radio(label='Select Order Type', options=['All', 'Un-delivered'], key='reb2',horizontal=True)
        ods, col_names = orders.getOrder_timeframe(timeframe)
        df = DataFrame(data=ods, columns=col_names)
        if rb2 == 'All':
            mem = df
            #df = df.loc[df['Delivery Status'] == "U"]
            df1 = con3.dataframe(data=df, use_container_width=True, on_select='rerun' ,selection_mode='single-row')
            sel1 = df1["selection"]['rows']
        if rb2 == 'Un-delivered':
            x = df.reset_index(drop=True, inplace=False)
            df1 = con3.dataframe(data=x, use_container_width=True, on_select='rerun' ,selection_mode='single-row')
            mem = x

    if sel1 != []:
        con3.success("Order {} selected".format(mem.loc[sel1[0]].at['Order ID']))
        b_col1,b_col2,b_col3 = con3.columns(3)
        b1 = b_col1.button(label="Mark as Delivered", key='bd12')
        if b1:
            if mem.loc[sel1[0]].at['Delivery Status'] == 'D':
                st.warning("Order Already Delivered")
            else:
                if orders.mark_delivery(status="D", order_id=mem.loc[sel1[0]].at['Order ID']):
                    st.success("Order Marked as Delivered")
                    tf.sleep(5)
                    st.rerun()
                    
                else:
                    st.warning("Action Failed, Try Again")