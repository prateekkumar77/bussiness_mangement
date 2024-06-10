import streamlit as st
from features import reset, getProductList

cart = 0


def app():
  global cart


## Order Page UI

  st1 = "IN 🧺 Cart {} item(s) ".format(str(cart))
  st.header("🥡 :orange[Orders Manager] ")

  st.markdown("<h2>"+st1+"<h2>",unsafe_allow_html=True)

  products = getProductList()
  no_products = len(products)
  reqRows = no_products // 4

  if no_products % 4 !=0:
    reqRows = (no_products // 4) + 1
  
  rows = []

# Menu GRID UI 
  expan1 = st.expander("Category 1")

  con1 = expan1.container()
  k = 0
  for r in range(reqRows):
    col = con1.columns(4)
    for c in range(4):
      if k >= no_products:
        break
      key1 = "p" + str(k)
      key2 = "q" + str(k)
      col[c].text(products[k])
      
      c1 = col[c].checkbox("Add to Cart",key=key1,)
      q1 = col[c].number_input(label="Quantity", max_value=5,min_value=1,value=1,key=key2)
      rows.append([c1,q1,products[k]])
      k += 1

#Cart Value Calculation
  p = 0
  x = False

  for r in range(no_products):
    if rows[r][0]:
      p += rows[r][1]
    if x is False and rows[r][0] is True:
      x = True
  

  if not x:
    p = 0
  
  if cart != p:
    cart = p
    st.rerun()


#Reset Button
  col1,col2,col3 = st.columns(3)
  button1 = col1.button("Reset", key='reset', on_click=reset)

