# -*- coding: utf-8-*-
import logging
from notifier import Notifier
from brain import Brain
import cercaIP
import re
import Pyro4
import os
import time
import signal

logging.basicConfig()

IP=cercaIP.cerca()
Buffer=Pyro4.Proxy("PYRO:jasper.Buffer@%s:5181"%(IP))
diferentsMicrofons=Pyro4.Proxy("PYRO:jasper.diferentsMicrofons@%s:5161"%(IP))
comprovaConnexio=Pyro4.Proxy("PYRO:jasper.comprovaConnexio@%s:5166"%(IP))
config=Pyro4.Proxy("PYRO:jasper.Config@%s:5111"%(IP))


IP_MASTER=comprovaConnexio.valor_actual()
comandesGlobals=Pyro4.Proxy("PYRO:jasper.comandesGlobals@%s:5164"%(IP_MASTER))


diferentsMicrofons.modifica_pregunta(0)
diferentsMicrofons.modifica(0)
comandesGlobals.modifica_ocupat(0)

def signal_handler(signum, frame):

    raise Exception("Timed out!")
	    

def executar(comanda,num_mic,text):

	linia=comanda[0]
	IP=comanda[1]
	executaComandes=Pyro4.Proxy("PYRO:jasper.executaComanda@%s:5163"%(IP))
	executaComandes.executa("%s '%s' '%s' '%s' '%s' &"%(linia,IP_MASTER,IP,num_mic,text))

def adaptar_caracters(paraula):
	

	paraula=paraula.encode('utf-8')
	d={"\xc3\x81":"A","\xc3\x89":"E","\xc3\x8d":'I',"\xc3\x91":'N',"\xc3\x93":"O","\xc3\x9a":"U"}
	for el in d.keys():
		if el in paraula:
			paraula=paraula.replace(el,d[el])
	return str(paraula)


def esValid(word,text):

	word=word.split()
	for el in word:

		if el in text:

			pass
		else:
			return False

	return True

def comanda(text):
	
	diccionari=comandesGlobals.valor_actual()
	words=diccionari.keys()
	for word in words:

		if esValid(word,text):
			return diccionari[word][0].strip(),diccionari[word][1].strip()
	return None

def triarMic(mic):

	configuracio=config.valor_actual()
	T=configuracio[6]
	if T=='witaiE':
		return mic[0],0
	elif T=='witaiC':
		return mic[1],1
	elif T=='googleE':
		return mic[2],2
	elif T=='googleC':
		return mic[3],3
	elif T=='attE':
		return mic[4],4
	elif T=='attC':
		return mic[5],5


class Conversation(object):

    def __init__(self, persona, mic0,mic1,mic2,mic3,mic4,mic5):
      
        self.persona = persona
	self.opcions=[mic0,mic1,mic2,mic3,mic4,mic5]
        self.mic,self.num_mic = triarMic(self.opcions)
	
       
    def handleForever(self):

	self.mic.say('Iniciando sistema de control por voz.')       

        while True:

		signal.signal(signal.SIGALRM, signal_handler)
		signal.setitimer(signal.ITIMER_REAL,25) 

		try:

			self.mic,self.num_mic=triarMic(self.opcions)
			if diferentsMicrofons.valor_actual_pregunta()==0:

			    threshold, transcribed = self.mic.passiveListen(self.persona)
			    print transcribed
			    Buffer.modifica_valor(transcribed)
			   
			    if not transcribed or not threshold:
				
				continue
					
			    diferentsMicrofons.modifica_pregunta(1)

			elif diferentsMicrofons.valor_actual()==1:
		
				diferentsMicrofons.modifica_pregunta(0)			
				diferentsMicrofons.modifica(0)

				signal.signal(signal.SIGALRM, signal_handler)
				signal.setitimer(signal.ITIMER_REAL,15) 
				
				try:
	
					text = self.mic.activeListenToAllOptions(threshold)
					if text=='':
						self.mic.say("No se ha detectado voz.")
					else:
						print text
						text=adaptar_caracters(text[0])
						Buffer.modifica_valor(text)
						ordre=comanda(text)
						executar(ordre,self.num_mic,text)

				except:

					self.mic.say("Tengo problemas con esta operacion.")

				comandesGlobals.modifica_ocupat(0)						

		except Exception,msg:

			print 'Error tipus 1'
			signal.setitimer(signal.ITIMER_REAL,0)	
			comandesGlobals.modifica_ocupat(0)
			diferentsMicrofons.modifica_pregunta(0)			
			diferentsMicrofons.modifica(0)		
			time.sleep(5)


		except:

			print 'Error tipus 2'
			signal.setitimer(signal.ITIMER_REAL,0)
			comandesGlobals.modifica_ocupat(0)
			diferentsMicrofons.modifica_pregunta(0)			
			diferentsMicrofons.modifica(0)
			self.mic.say("Se ha detectado un error desconocido.")
			time.sleep(5)

		signal.setitimer(signal.ITIMER_REAL,0)

		
				
