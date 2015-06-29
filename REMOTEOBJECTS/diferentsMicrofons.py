import Pyro4
import os
import  cercaIP

class diferentsMicrofons():
	
	def __init__(self):
		self.indicadora=0
		self.pregunta=0

	def valor_actual(self):
		return self.indicadora

	def valor_actual_pregunta(self):	
		return self.pregunta

	def modifica(self,numero):
		self.indicadora=numero

	def modifica_pregunta(self,numero):
		self.pregunta=numero

diferentsMicrofons=diferentsMicrofons()
Pyro4.Daemon.serveSimple({diferentsMicrofons:"jasper.diferentsMicrofons"},port=5161,host=cercaIP.cerca(),ns=False)
