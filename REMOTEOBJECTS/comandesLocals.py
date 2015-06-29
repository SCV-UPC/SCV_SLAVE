import Pyro4
import os
import cercaIP
from actualitzaComandesLocals import cerca

IP=cercaIP.cerca()
	
class comandesLocals():
	
	def __init__(self):
		self.comandes=cerca()

	def valor_actual(self):
		return self.comandes

	def modifica_valor(self,variable):
		self.comandes=variable

comandesLocals=comandesLocals()
Pyro4.Daemon.serveSimple({comandesLocals:"jasper.comandesLocals"},port=5162,host=IP,ns=False)

