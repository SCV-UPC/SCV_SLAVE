import Pyro4
import os
import cercaIP

class comprovaConnexio():
	"""
	Aquesta classe permet a la Raspberry Master coneixer quines Raspberry's estan
	funcionant a aquell moment. Tambe es guarda el valor de la ip de la Raspberry 
	MASTER (l'escriu la propia MASTER quan fa un escombrat de ip's).
	"""	
	def __init__(self):

		self.IP_MASTER=''

	def valor_actual(self):

		return self.IP_MASTER

	def modifica_valor(self,IP):

		self.IP_MASTER=IP

	def comprova(self):

		return 0

comprovaConnexio=comprovaConnexio()
Pyro4.Daemon.serveSimple({comprovaConnexio:"jasper.comprovaConnexio"},port=5166,host=cercaIP.cerca(),ns=False)

