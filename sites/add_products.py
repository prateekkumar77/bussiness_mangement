import streamlit as st
from features import html_clear_input
from streamlit.components.v1 import html
from models import product
import logging

#Defining error and info loggers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger1 = logging.getLogger(__name__)
logger1.setLevel(logging.INFO)

        # Log to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger1.addHandler(handler)

        # Also log to a file
file_handler = logging.FileHandler("logs/app-logs.log")
file_handler.setFormatter(formatter)
logger1.addHandler(file_handler)
# END LOGGER DEFINATION

def app():
    st.header("🎁 :orange[Add New Product]",divider=True)
    st.markdown("")

    con1 = st.container()
    col1,col2, = con1.columns(2)
    p_code = col1.text_input(label="Product Code",max_chars=5,key="p_code", placeholder="PO-XXX",value="")
    p_name = col2.text_input(label="Product Name", max_chars=20, key='p_name', placeholder="Enter Product Name")
    img_url = con1.text_input(label="Product Image URL", max_chars=100, key='p_url', placeholder="Enter Image URL")
    col3,col4 = con1.columns(2)
    category = col3.selectbox(label="Select Category",key='cat',options=[None, 'Detox Drink', 'Detox Bowl', 'Overnight-Oats', 'Fat-loss Dinner', 'Other'])
    p_price = col4.number_input(label="Enter Price",min_value=1,value=50,key='p_inp')
    p_decription = con1.text_input(label="Product Description",max_chars=150, key='p_desc',placeholder="Enter Product Description")
    
    c1,c2 = con1.columns(2)
    b1 = c1.button(label="Reset", key='r-button',use_container_width=True,disabled=True)
    b2 = c2.button(label="Add Product", key='add-button',use_container_width=True)

    if b1:
        st.rerun()
        #st.markdown(html_clear_input,unsafe_allow_html=True)

    if b2:
        new_product = product(id=p_code,name=p_name,description=p_decription,price=p_price,img_url=img_url,category=category)
        res = new_product.add_product_toDB(logger1)

        if res:
            logger1.info('New Product added '+p_name+" "+p_code)
            st.success("Product Added")
            st.success(p_name)
        else:
            logger1.error("Product addition failed")
            st.warning("Product addition failed")