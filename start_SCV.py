import os
import time

os.system("python /home/pi/SCV/REMOTEOBJECTS/comandesLocals.py &")
os.system("python /home/pi/SCV/REMOTEOBJECTS/diferentsMicrofons.py &")
os.system("python /home/pi/SCV/REMOTEOBJECTS/executaComandes.py &")
os.system("python /home/pi/SCV/REMOTEOBJECTS/comprovaConnexio.py &")
os.system("python /home/pi/SCV/REMOTEOBJECTS/buffer.py &")
os.system("python /home/pi/SCV/REMOTEOBJECTS/fitxer.py &")
os.system("python /home/pi/SCV/CONFIGURATION/config.py &")

time.sleep(30)
os.system("python /home/pi/SCV/REMOTEOBJECTS/temporitzador1.py &")
os.system("python /home/pi/SCV/CONFIGURATION/temporitzador5.py &")

time.sleep(30)
os.system("python /home/pi/SCV/JASPER2/Jasper2_remot.py &")

time.sleep(10)
os.system("python /home/pi/SCV/JASPER2/Jasper2.py")







