import streamlit as st


def app():
  st.header("🏠 :green[Bussiness Overview]",divider=True)



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