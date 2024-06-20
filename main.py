import streamlit as st
from streamlit_option_menu import option_menu
from sites import home ,account, clients, orders, delivery,register_client, add_products, manage_orders
from features import html_light_mode,html_dark_mode,html_style_theme_switch


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

st.markdown(html_style_theme_switch,unsafe_allow_html=True)

st.markdown(html_light_mode,unsafe_allow_html=True)


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
                            'Home', 'Account', 'Members', 'New Order', 'Manage Delivery', 'Add Member', 'Add Products', 'Manage Orders'],
                        icons=[
                            'house-fill', 'person-circle', 'people-fill', 'cart-plus', 'bicycle','person-fill-add','plus-square-fill','layout-text-window-reverse'],
                        menu_icon='cast',
                        default_index=0,
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
    if app == "Members":
      clients.app()
    if app == "New Order":
      orders.app()
    if app == "Manage Delivery":
      delivery.app()
    if app == "Add Member":
      register_client.app()
    if app == "Add Products":
      add_products.app()
    if app == "Manage Orders":
      manage_orders.app()

  run()
