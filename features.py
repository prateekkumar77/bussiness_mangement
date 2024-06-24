import streamlit as st
import logging
import urllib.request
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt


formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

def get_line_sale_chart(data:list, colums:list, grid:bool=False, data2:list=None, compare:bool=False):
    fig, ax = plt.subplots(figsize=(10,7))
    ax.plot(colums,data, marker='o', linestyle='-.', color='green')
    ax.grid(grid)
    ax.set_title("Sale Throughout the Week")
    ax.set_ylabel("No. of Products Sold")
    #ax.annotate("34",xy=(data[0],0), xytext=(data[0],0))
    #ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
     #       arrowprops=dict(facecolor='black', shrink=0.05),
      #      )
    if data2 is not None and compare:
        ax.plot(colums,data2, marker='o', linestyle='-.', color='red')
    return fig

def get_bar_chart(data:list, columns:list, legend:bool=False):
    fig, ax = plt.subplots(figsize=(6,4))

    #fruits = ['apple', 'blueberry', 'cherry', 'orange']
    #counts = [40, 100, 30, 55]
    #bar_labels = ['Jeevan', 'Amrit', 'Urja', 'Tript']
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

    ax.bar(columns, data,label=columns , color=bar_colors)

    ax.set_ylabel('Products Sold')
    ax.set_title('Most Selling Products')
    if legend:
        ax.legend(title='Produtcs')
    return fig


def get_fig_pie_plot_for_subscriber(data:list,legend:bool=False):
    y = data
    labels1 = ['Subscribed', 'Un-subscribed']
    exp1 = [0.2,0.1]

    fig1, ax1 = plt.subplots(figsize=(4,5))
    ax1.pie(y, explode=exp1, labels=labels1, autopct='%1.1f%%',
        shadow=True, startangle=90)
    if legend:
        ax1.legend()
    ax1.set_title('Subscriptions Overview')
    ax1.axis('equal')
    return fig1

def getImage(url:str,name:str):
   urllib.request.urlretrieve(url, "temp/{}.png".format(name))
   img = Image.open("temp/{}.png".format(name))
   return img

def initialize_logger(module_name:str=__name__) -> logging.getLoggerClass:
    
    #Defining error and info loggers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    logger1 = logging.getLogger(module_name)
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

    return logger1


html_style_theme_switch = """
        <style>
        body {
            padding: 25px;
            background-color: white;
            color: black;
            font-size: 25px;
        }

        .dark-mode {
            background-color: black;
            color: white;
        }

        .light-mode {
            background-color: white;
            color: black;
        }
    </style>
        """

html_dark_mode= """
<script>
            let element = document.body;
            element.className = "dark-mode";
    </script>
        
       """
html_light_mode = """
<script>
            let element = document.body;
            element.className = "light-mode";
</script>
"""

html_clear_input = """
<script>
        location.reload();

</script>
"""


def search(item:str) -> list[str]:
    pass

def add_to_excel(value:str, row=None, col=None) -> bool:
    pass


def getProductList() ->list:
  return ['Product1' , 'Product2', 'Product3', 'Product4', 'Product5', 'Product6','Product7', 'Product8', 'Product9']

def reset() ->None:
  global cart
  cart = 0
  st.session_state.p0 = False
  st.session_state.p1 = False
  st.session_state.p2 = False
  st.session_state.p3 = False
  st.session_state.p4 = False
  st.session_state.p5 = False
  st.session_state.p6 = False
  st.session_state.p7 = False
  st.session_state.p8 = False
  st.session_state.p9 = False
  st.session_state.p10 = False
  st.session_state.check1 = False
  st.session_state.date_cb = False
  #st.session_state.sb2 = None
  st.session_state.ins1 = None
