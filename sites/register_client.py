import streamlit as st


def app():
        st.header("📝 :orange[Client Registration]")
        #st.markdown("<h2 style= 'text-align: center'>Client Registration<h2>", unsafe_allow_html=True)
        container1 = st.container()
        col1,col2 = container1.columns(2)
        name = col1.text_input(label="Name")
        email = col2.text_input(label="Email ID")
        phn = col1.text_input(label="Phone No.")
        col2.checkbox(label="Subcribed")
        add = container1.text_input("Address")
        submit1 = container1.button("Submit",use_container_width=True,type="primary")
        if submit1:
                if name == "" or email == "" or phn == "" or add == "":
                    st.warning("Please fill all the above fields")
                else:
                    st.success("Registered Successfully")