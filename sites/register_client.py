import streamlit as st
from models import client
import datetime, random
from features import initialize_logger

logger = initialize_logger(__name__)
client1 = client()

def app():
        st.header("📝 :orange[Client Registration]",divider=True)
        #st.markdown("<h2 style= 'text-align: center'>Client Registration<h2>", unsafe_allow_html=True)
        st.markdown("")
        container1 = st.container()
        col1,col2 = container1.columns(2)
        name = col1.text_input(label="Full Name", max_chars=50,placeholder="Enter Full Name")
        email = col2.text_input(label="Email ID",max_chars=50,placeholder="example@gmail.com")
        phn = col1.text_input(label="Phone No.",max_chars=10,placeholder="9XX-XXXX-XX9")
        cb1 = col2.checkbox(label="Subcribed",key="cb1")
        plan = ""
        if cb1:
             c1,c2 = container1.columns(2)
             plan = c1.selectbox(label="Select a Plan", options=[None]+["Plan1", "Plan2", "Plan3"],placeholder="Select a Plan",)
             end_date = c2.date_input(label="Plan End-Date",min_value=datetime.date.today(),key="end_date",help="End Date should be atleast a week from now")
             #print(plan)
        col3,col4 = container1.columns(2)
        flat_no = col3.text_input(label="Flat No.",max_chars=10,placeholder="Enter Flat No.")
        society = col4.selectbox("Select Society", options=[None, "Society 1", "Society 2"])
        add = container1.text_input("Address",max_chars=50)
        submit1 = container1.button("Submit",use_container_width=True,type="primary")
        if submit1:
                if name == "" or email == "" or phn == "" or add == "":
                    st.warning("Please fill all the above fields")
                else:
                    c_id = "CL"
                    c_id += str(random.randint(60000,99999))
                    if cb1:
                          subs = "N"
                          end_date = "N/A"
                          plan = "N/A"
                    else:
                          subs = "Y"
                          end_date = str(end_date)

                    cl = client(name=name,client_id=c_id, subscribed=subs,end_date=end_date,flat_no=flat_no,society=society,address1=add,email_id=email,phn_no=phn,plan=plan)
                    if client.save():
                        logger.info("New Client Data saved to DB ({})".format(name))
                        st.success("Registered Successfully [Client:{}]")
                    else:
                          logger.warning("Registration Failed for {}".format(name))
                          st.warning("Registration Failed. Please try again!")
                        