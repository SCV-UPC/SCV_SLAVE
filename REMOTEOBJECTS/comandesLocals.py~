import Pyro4
import os
import cercaIP
from actualitzaComandesLocals import cerca

IP=cercaIP.cerca()
	
class comandesLocals():
	"""
	Aquesta classe fa que les comandes al fitxer comandes.txt siguin accessibles des de tot arreu,
	creant un objecte remot. Per tant, totes les altres Raspberry's tindran acces al seu
	arxiu comandes.txt, que conte totes les paraules o conjunt de paraules a detectar amb les seves 
	respectives accions.
	"""
	def __init__(self):

		self.comandes=cerca()

	def valor_actual(self):

		return self.comandes

	def modifica_valor(self,variable):
	
		self.comandes=variable

comandesLocals=comandesLocals()
Pyro4.Daemon.serveSimple({comandesLocals:"jasper.comandesLocals"},port=5162,host=IP,ns=False)

