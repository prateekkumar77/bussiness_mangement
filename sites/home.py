import streamlit as st
from database import get_live_db_object, MYSQL_USER, HOST, DATABASE_NAME
from features import initialize_logger

logger1 = initialize_logger(__name__)


def app():
    st.header("🏠 :green[Bussiness Overview]",divider=True)
    b1 = st.button("Check DB")

    if b1:
        logger1.info("DB Connection Check initiated")
        db = get_live_db_object()
        if db is not False:
            st.success("Database Connection Successful")
            #print("Success")
            st.markdown("DB Config")
            st.json({"DB Host":HOST, "DB Name":DATABASE_NAME, "User":MYSQL_USER},expanded=False)
            db.close()
        else:
            st.warning("Unable to connect to DB. Check DB config")

