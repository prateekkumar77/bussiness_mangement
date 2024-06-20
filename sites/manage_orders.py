import streamlit as st
from streamlit_searchbox import st_searchbox
from models import client

def app():
    st.header(" :orange[Manage Orders]",divider="gray")

    #col1,col2 = st.columns(2)
    con1 = st.container()
    cb1 = con1.radio(label='Search Filter', options=['Find by Time', 'Find by Client'], key='rd1', horizontal=True)
    val = None
    if cb1 == 'Find by Time':
        #val = None
        col1,col2 = con1.columns(2)
        b1 = col1.radio(label="Select", key='r3', options=['Today', 'Yesterday', 'Custom'])
        #b2 = col1.button(label="Yesterday", key='b2', use_container_width=True)
        if b1 == 'Custom':
            d1 = col2.date_input(label="Choose Date", key='date1')
            #b3 = col2.button(label="Select", key='b3', use_container_width=True)
        b3 = con1.button(label="Search", key='b3',)
    if cb1 == 'Find by Client':
        val = st_searchbox(label="Search Client", search_function=client.search_client, key="sb2", placeholder="Search All Clients")

    if val is not None:
        pass