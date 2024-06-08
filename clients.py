import streamlit as st

clients = []
totalClients = 117 #len(clients)
change = 23

if change < 0:
  change = '-' + str(change)
else:
  change = "+" + str(change)


def app():
  st.header("Client Data Manager")

  st.metric(label="Total Clients", value=totalClients, delta=change, help="Value in color represent the change in numbers in within a week")

  addClientBtn = st.button(label="Register", on_click=addClient)
  

def addClient():
    with st.container():
        st.markdown("<h1 style= 'text-align: center'>Client Registration<h1>", unsafe_allow_html=True)
        with st.form("Register a Client"):
            col1,col2 = st.columns(2)
            name = col1.text_input(label="Name")
            email = col2.text_input(label="Email ID")
            phn = col1.text_input(label="Phone No.")
            col2.checkbox(label="Subcribed")
            add = st.text_input("Address")
            submit1 = st.form_submit_button("Submit")
            if submit1:
                if name == "" or email == "" or phn == "" or add == "":
                    st.warning("Please fill all the above fields")
                else:
                    st.success("Registered Successfully")