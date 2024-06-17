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
            st.json({"DB Host":HOST, "DB Name":DATABASE_NAME, "User":MYSQL_USER})
            db.close()
        else:
            st.warning("Unable to connect to DB. Check DB config")


html = """
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

htm2_dark_mode= """
<script>
            let element = document.body;
            element.className = "dark-mode";
    </script>
        
       """
hmtl_light_mode = """
<script>
            let element = document.body;
            element.className = "light-mode";
</script>
"""