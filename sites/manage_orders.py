import streamlit as st, datetime
from streamlit_searchbox import st_searchbox
from models import client, orders
from pandas import DataFrame
import time as tf

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
        val = None
        if time == 'Today':
            time = str(datetime.date.today())
        elif time == 'Yesterday':
            time = str(datetime.date.today() - datetime.timedelta(1))
        else:
            time = str(time)
            
    
    st.markdown(" ")
    con2 = st.container()
    sel1 = ""
    ods = []
    new_df = []
    #rb2 = con2.radio(label='Select Order Type', options=['All', 'Unpaid'], key='rb2')
    if val is not None and val != "None":
        cc1,cc2 = con2.columns(2)
        rb2 = cc1.radio(label='Select Order Type', options=['All', 'Unpaid'], key='rb2',horizontal=True)
        ods, col_names = orders.getOrders_cID(val.split(":")[2].lstrip().rstrip())
        df = DataFrame(data=ods, columns=col_names)
        #cc2.metric(label="No. of Orders", value=df.shape[0])
        new_df = df
        if rb2 == 'All':
            x = con2.dataframe(data=df, use_container_width=True, on_select='rerun' ,selection_mode='single-row')
            #st.success(str(x))
            cc2.metric(label="No. of Orders", value=df.shape[0])
        if rb2 == 'Unpaid':
            new_df = df.loc[df['Payment Status'] == "U"]
            x1 = new_df.reset_index(drop=True,inplace = False)
            x = con2.dataframe(data=x1, use_container_width=True, on_select='rerun' ,selection_mode='single-row')
            cc2.metric(label="No. of Orders", value=x1.shape[0])
            new_df = x1

        sel1 = x["selection"]['rows']
        #print("sel1 :{}".format(sel1))

    if time is not None:
        cc1,cc2 = con2.columns(2)
        rb2 = cc1.radio(label='Select Order Type', options=['All', 'Unpaid'], key='rb3',horizontal=True)
        ods, col_names = orders.getOrder_timeframe(time)
        df = DataFrame(data=ods, columns=col_names)
        #cc2.metric(label="No. of Orders", value=df.shape[0])
        new_df = df
        if rb2 == 'All':
            x = con2.dataframe(data=df, use_container_width=True, on_select='rerun' ,selection_mode='single-row',key='df2')
            #st.success(str(x))
            cc2.metric(label="No. of Orders", value=df.shape[0])
        if rb2 == 'Unpaid':
            new_df = df.loc[df['Payment Status'] == "U"]
            x1 = new_df.reset_index(drop=True,inplace = False)
            x = con2.dataframe(data=x1, use_container_width=True, on_select='rerun' ,selection_mode='single-row',key='df2')
            cc2.metric(label="No. of Orders", value=x1.shape[0])
            new_df = x1

        sel1 = x["selection"]['rows']
        pass

    if sel1 != [] and sel1 != "":
        con2.success("Order {} selected".format(new_df.loc[sel1[0]].at['Order ID']))

        b_col1,b_col2,b_col3 = con2.columns(3)
        flag = False
        if new_df.loc[sel1[0]].at['Payment Status'] == 'P':
            flag = True
        else:
            pass

        b1 = b_col1.button(label="Mark as Paid", key='b12', disabled=flag, use_container_width=True)
        b2 = b_col2.button(label="Mark Un-Paid", key='bb2', disabled=not flag, use_container_width=True)
        b3 = b_col3.button(label="Delete", key='d-b3', use_container_width=True)

        if b1:
            if orders.mark_as_paid(new_df.loc[sel1[0]].at['Order ID']):
                st.success("Order Marked as PAID")
                tf.sleep(5)
                st.rerun()                    
            else:
                st.warning("Action Failed, Try Again")
        