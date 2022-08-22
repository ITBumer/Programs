import socket
import json
import pymysql
import datetime
from Conect import connection

now = datetime.datetime.now()

server = socket.socket (

    socket.AF_INET,
    socket.SOCK_STREAM,
)

server.bind(
    ("185.93.110.41", 7000) # Прописать свой сервер
)

server.listen(5)
print("Server listening !")

while True:
    user_socket, address = server.accept()
    user_socket.send("You are connected !".encode("utf - 8"))
    data = user_socket.recv(2048)
    data_res = json.loads(data.decode("utf-8"))
    print(data_res)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO SENSOR_MES (DATE_TIME,MESSAGE) VALUES (%s,%s)", (now,data_res))
    connection.commit()
