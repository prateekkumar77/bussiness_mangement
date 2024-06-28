import streamlit as st
import datetime
from streamlit_searchbox import st_searchbox
from models import client
from pandas import DataFrame
from models import orders
import time as tf
from features import initialize_logger

logger = initialize_logger(__name__)

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
    

    sel1 = []
    mem = []
    con2 = st.container()
    con3 = st.container()


    if val is not None and val != "None":
        timeframe = None
        con2.success("Selected Member : {}".format(val.split(":")[0]))
        cc1,cc2 = con2.columns(2)
        rb2 = cc1.radio(label='Select Order Type', options=['All', 'Un-Delivered'], key='rb2',horizontal=True)
        ods, col_names = orders.getOrders_cID(val.split(":")[2].lstrip().rstrip())
        df = DataFrame(data=ods, columns=col_names)
        if rb2 == 'All':
            mem = df
            x = con3.dataframe(data=df, use_container_width=True, on_select='rerun' ,selection_mode='single-row')
            cc2.metric(label="No. of Delivery", value=df.shape[0])
        if rb2 == 'Un-Delivered':
            new_df = df.loc[df['Delivery Status'] == "U"]
            x1 = new_df.reset_index(drop=True,inplace = False)
            x = con3.dataframe(data=x1, use_container_width=True, on_select='rerun' ,selection_mode='single-row')
            cc2.metric(label="No. of Delivery", value=x1.shape[0])
            mem = x1
        sel1  = x["selection"]['rows']


    
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
        ods, col_names = orders.getOrder_timeframe2(timeframe)
        df = DataFrame(data=ods, columns=col_names)
        if rb2 == 'All':
            mem = df
            #df = df.loc[df['Delivery Status'] == "U"]
            df1 = con3.dataframe(data=df, use_container_width=True, on_select='rerun' ,selection_mode='single-row')
            sel1 = df1["selection"]['rows']
            cc2.metric(label="No. of Delivery", value=df.shape[0])
        if rb2 == 'Un-delivered':
            df = df.loc[df['Delivery Status'] == "U"]
            x = df.reset_index(drop=True, inplace=False)
            df1 = con3.dataframe(data=x, use_container_width=True, on_select='rerun' ,selection_mode='single-row')
            sel1 = df1["selection"]['rows']
            cc2.metric(label="No. of Delivery", value=df.shape[0])
            mem = x
    
    flag = False

    if sel1 != []:
        if mem.loc[sel1[0]].at['Delivery Status'] == 'D':
                flag = True
        con3.success("Order {} selected".format(mem.loc[sel1[0]].at['Order ID']))
        b_col1,b_col2 = con3.columns(2)
        b1 = b_col1.button(label="Mark as Delivered", key='bd12',use_container_width=True, disabled=flag)
        b2 = b_col2.button(label='Mark as Un-Delivered', key='bd13', use_container_width=True, disabled= not flag)
        if b1:
                if orders.mark_delivery(status="D", order_id=mem.loc[sel1[0]].at['Order ID']):
                    st.success("Order Marked as Delivered")
                    tf.sleep(5)
                    st.rerun()
                    
                else:
                    st.warning("Action Failed, Try Again")
                    logger.warning("Delivery Marking Failed")

        if b2:
                if orders.mark_delivery(status="U", order_id=mem.loc[sel1[0]].at['Order ID']):
                    st.success("Order Marked as Delivered")
                    tf.sleep(5)
                    st.rerun()
                    
                else:
                    st.warning("Action Failed, Try Again")
                    logger.warning("Delivery Marking Failed")