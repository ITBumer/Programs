#!/usr/bin/python3

import json
import socket
import smtplib
import subprocess
import time
import datetime


result = subprocess.check_output('df -h | grep /dev/mmcblk0p2', shell=True).decode('utf -8')

mean = int(result[-7:-4])

while mean > 80:

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("diag.py@gmail.com", "qwerty%21")
        someVariable = "Attention !!! the system is filled with "+str(mean)+" %"
        server.sendmail("diag.py@gmail.com","ruslan.viantec@gmail.com","{}".format(someVariable))
        server.quit()
        time.sleep(60*30)
        # В данном цикле происходит проверка дискового пространства, если значение превышает требуемое то происходит отправка сообщения на почту.



res = subprocess.check_output('systemctl status rubin | grep running',shell=True)
index = res.find(("active (running)").encode('utf-8'),13,29)

if  index==13:
    time.sleep(1)
    print("Process 1 OK!")


else:

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM,)
    client.connect(("185.93.110.41", 7000))
    data = client.recv(2048)
    mes = "Process 1 error !"
    mesg = json.dumps(mes)
    client.send((mesg).encode("utf-8"))
    print("launch !")
    time.sleep(2)
    subprocess.check_output('systemctl start rubin', shell=True)
    time.sleep(60)


res2 = subprocess.check_output('ps auxww | grep airodump', shell=True)
indexStat = res2.find(("Sl+").encode('utf-8'),1,60)

if indexStat != -1:
    time.sleep(1)
    print("Process 2 OK!")

else:

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM,)
    client.connect(("185.93.110.41", 7000))
    data = client.recv(2048)
    mes = "Process 2 error !"
    mesg = json.dumps(mes)
    client.send((mesg).encode("utf-8"))
    print("launch !")
    time.sleep(2)
    subprocess.check_output('systemctl start rubin', shell=True)
    time.sleep(60)



now = datetime.datetime.now().strftime('%b %d %H:%M')
res3 = subprocess.check_output('ls -laht /tmp/capture1-01.csv', shell=True)
indexNow = res3.find((now+" /tmp/capture1-01.csv").encode('utf-8'),5,63)


if  indexNow !=-1:
    time.sleep(1)
    print("Process 3 OK!")
else:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM,)
    client.connect(("185.93.110.41", 7000))
    data = client.recv(2048)
    mes = "Process 3 error !"
    mesg = json.dumps(mes)
    client.send((mesg).encode("utf-8"))
    print("launch !")
    time.sleep(2)
    subprocess.check_output('systemctl start rubin', shell=True)
    time.sleep(60)
