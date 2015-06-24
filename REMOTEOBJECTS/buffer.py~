import Pyro4
import cercaIP

IP=cercaIP.cerca()
	
class Buffer():
	

	def __init__(self):

		self.buffer='Iniciant...'

	def valor_actual(self):

		return self.buffer

	def modifica_valor(self,variable):
	
		self.buffer=variable

Buffer=Buffer()
Pyro4.Daemon.serveSimple({Buffer:"jasper.Buffer"},port=5181,host=IP,ns=False)

