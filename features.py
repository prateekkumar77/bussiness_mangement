import streamlit as st
import logging

def log_info(module_name:str=__name__) -> logging:
    
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Log to console
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also log to a file
    file_handler = logging.FileHandler("app-logs.log")
    file_handler.setFormatter(formatter)
    logger.info.addHandler(file_handler)

    return logger

def log_error(module_name:str=__name__) -> logging:
    
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Log to console
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also log to a file
    file_handler = logging.FileHandler("app-logs.log")
    file_handler.setFormatter(formatter)
    logger.info.addHandler(file_handler)

    return logger

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
