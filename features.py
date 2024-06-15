import streamlit as st
import logging

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

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
