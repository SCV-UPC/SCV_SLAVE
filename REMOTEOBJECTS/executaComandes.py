import Pyro4
import os
import cercaIP

class executaComanda():
	
	def executa(self,comanda):
		os.system(comanda)

executaComanda=executaComanda()
Pyro4.Daemon.serveSimple({executaComanda:"jasper.executaComanda"},port=5163,host=cercaIP.cerca(),ns=False)



