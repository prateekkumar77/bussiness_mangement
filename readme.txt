venv path: /Users/prateekkumar77/Documents/bussiness_mangement/.venv/bin/python -m

Run using

/Users/prateekkumar77/Documents/bussiness_mangement/.venv/bin/python -m streamlit run main.py 


pip freeze > requirements.txt


streamlit run streamlit_app.py --server.port 8080


Theme

[theme]
base="dark"
primaryColor="#bd2d91"
backgroundColor="#20201f"
secondaryBackgroundColor="#5d5f6b"
font="monospace"



Mysql
SET time_zone = "+05:30";


Attach Mysql Server

docker run --name mysql -d \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=root-pass\
    -v mysql:/var/lib/mysql \
    mysql:latest