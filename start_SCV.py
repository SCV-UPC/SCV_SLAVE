#ADAPTACIO D'UN HABITATGE A PERSONES AMB PROBLEMES DE MOBILITAT MITJANcANT
#CONTROL PER VEU.

#Treball fi de Grau en Tecnologies Industrials. Propietat d'Eduard Godori
#i UPC.

#aquest fitxer es modifica en funcio del tipus de maquina que es necessita. 
#Esta directament relacionat amb el tipus d'instal.lacio que s'hagi fet.
#Per tal d'arrencar correctament el sistema cal seguir els comentaris que
#es mostren a continuacio i descomentar aquella part del codi necessaria. 
#Els time.sleep poden ser indispensables. L'ordre es molt important.


import os
import time

#Qualsevol maquina que es vulgui connectar al SCV:

os.system("python /home/pi/SCV/REMOTEOBJECTS/comandesLocals.py &")
os.system("python /home/pi/SCV/REMOTEOBJECTS/diferentsMicrofons.py &")
os.system("python /home/pi/SCV/REMOTEOBJECTS/executaComandes.py &")
os.system("python /home/pi/SCV/REMOTEOBJECTS/comprovaConnexio.py &")
os.system("python /home/pi/SCV/REMOTEOBJECTS/buffer.py &")
os.system("python /home/pi/SCV/REMOTEOBJECTS/fitxer.py &")
os.system("python /home/pi/SCV/CONFIGURATION/config.py &")

#Els temporitzadors son opcionals, actualitzen automaticament en cas de 
#variacions als arxius de configuracio.

time.sleep(30)
os.system("python /home/pi/SCV/REMOTEOBJECTS/temporitzador1.py &")
os.system("python /home/pi/SCV/CONFIGURATION/temporitzador5.py &")

#La maquina MASTER:

os.system("python /home/pi/SCV/MASTER/cercaRaspberrys.py &")
time.sleep(60)
os.system("python /home/pi/SCV/MASTER/comandesGlobals.py &")
time.sleep(30)
os.system("python /home/pi/SCV/MASTER/temporitzador0.py &")
os.system("python /home/pi/SCV/MASTER/temporitzador2.py &")
os.system("python /home/pi/SCV/MASTER/temporitzador3.py &")
os.system("python /home/pi/SCV/WEBPAGE/temporitzador4.py &")
os.system("python /home/pi/SCV/MASTER/simulador.py &")

#Aquelles maquines que siguin receptores de so (JASPER2):

os.system("python /home/pi/SCV/JASPER2/Jasper2_remot.py &")
time.sleep(10)
#os.system("python /home/pi/SCV/JASPER2/Jasper2.py")







