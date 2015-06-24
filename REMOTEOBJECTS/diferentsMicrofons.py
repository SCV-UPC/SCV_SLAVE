import Pyro4
import os
import  cercaIP

class diferentsMicrofons():
	"""
	Aquesta classe te la funcio de buffer, es a dir, guarda el valor de la variable
	indicadora per tal de poder sincronitzar totes les Raspberry's que corren "jasper.py"
	per tal d'evitar que dos escoltin a la vegada. Gracies a aquest buffer el proces
	es sincron, per tal d'evitar possbiles errors. La variable indicadora val 0 si no s'ha 
	detectat la paraula clau i 1 en cas que s'hagi detectat.
	"""
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
