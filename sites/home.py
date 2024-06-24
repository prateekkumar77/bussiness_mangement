import streamlit as st
from database import get_live_db_object, MYSQL_USER, HOST, DATABASE_NAME
from features import initialize_logger, get_fig_pie_plot_for_subscriber, get_bar_chart,get_line_sale_chart
#import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np

logger1 = initialize_logger(__name__)


def app():
    st.header("🏠 :green[Bussiness Overview]",divider=True)
    b1 = st.button("Check DB")

    if b1:
        logger1.info("DB Connection Check initiated")
        db = get_live_db_object()
        if db is not False:
            st.success("Database Connection Successful")
            #print("Success")
            st.markdown("DB Config")
            st.json({"DB Host":HOST, "DB Name":DATABASE_NAME, "User":MYSQL_USER},expanded=False)
            db.close()
        else:
            st.warning("Unable to connect to DB. Check DB config")

    col1,col2 = st.columns(2)        

    expan1 = col1.expander("Subscription Overview")
    con1 = expan1.container()
    cb2 = con1.checkbox(label="Legend", key='cb_legend2')
    #col1,col2 = con1.columns(2)
    y = [42,35]
    fig1 = get_fig_pie_plot_for_subscriber(data=y,legend=cb2)
    con1.text("Susbcriber Overview")
    con1.pyplot(fig=fig1)
    expan2 = col2.expander("Most Selling Products")
    con2 = expan2.container()
    cb1 = con2.checkbox("Legend", key='chw2',)
    con2.text("Most Selling Products")
    quantity = [23, 32, 14, 17 ]
    prd_name = ["Jeevan", "Amrit" ,"Urja", "Tript"]
    fig2 = get_bar_chart(data=quantity,columns=prd_name,legend=cb1)
    con2.pyplot(fig=fig2)

    expan3 = st.expander("Sale Through Week")
    con3 = expan3.container()
    weekday = ['Monday', 'Tuesday' , 'Wednesday', 'Thrusday' , 'Friday' ,'Saturday']
    data1 = [23,64,30,32,54,34]
    data2 = [25, 53, 28, 41, 33, 29]
    c_col1, c_col2 = con3.columns(2)
    cb3 = c_col1.checkbox(label="Show Grid Lines", key='cd-gd')
    cb4 = c_col2.checkbox(label="Compare with Previous Week", key='gd-cd')
    fig3 = get_line_sale_chart(colums=weekday,data=data1,data2=data2,grid=cb3,compare=cb4)
    con3.pyplot(fig=fig3)
    
