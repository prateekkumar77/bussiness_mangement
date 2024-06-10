import streamlit as st


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
