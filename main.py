import streamlit as st
from streamlit_option_menu import option_menu
import home ,account, clients, orders

#x = st.image('logo.jpg', caption='Company Logo')

st.set_page_config(page_title="Rasamrit",
                  )

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


class MultiApp:

  def __init__(self) -> None:
    self.apps = []

  def add_app(self, title, function):
    self.apps.append({"title": title, "function": function})

  def run():
    # app = st.sidebar(
    with st.sidebar:
      app = option_menu(menu_title='All Apps ',
                        options=[
                            'Home', 'Account', 'Clients', 'Orders'],
                        icons=[
                            'house-fill', 'person-circle', 'people-fill', 'box-seam' ],
                        menu_icon='cast',
                        default_index=1,
                        styles={
                            "container": {
                                "padding": "5!important",
                                "background-color": 'black'
                            },
                            "icon": {
                                "color": "white",
                                "font-size": "23px"
                            },
                            "nav-link": {
                                "color": "white",
                                "font-size": "20px",
                                "text-align": "left",
                                "margin": "0px",
                                "--hover-color": "blue"
                            },
                            "nav-link-selected": {
                                "background-color": "#02ab21"
                            },
                        })

    if app == "Home":
      home.app()
    if app == "Account":
      account.app()
    if app == "Clients":
      clients.app()
    if app == "Orders":
      orders.app()

    

  run()
