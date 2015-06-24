import Pyro4
import cercaIP

IP=cercaIP.cerca()
	
class Simulador():
	

	def __init__(self):

		self.estat=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		self.temp=''
		self.alar=''
		self.chan=''

	def valor_actual(self):

		return self.estat

	def modifica_estat(self,var):
	
		self.estat=var

	def temperatura(self):

		return self.temp

	def modifica_temperatura(self,var):

		self.temp=var

	def alarma(self):

		return self.alar

	def modifica_alarma(self,var):

		self.alar=var

	def canal(self):

		return self.chan

	def modifica_canal(self,var):

		self.chan=var

	

simulador=Simulador()
Pyro4.Daemon.serveSimple({simulador:"jasper.Simulador"},port=5123,host=IP,ns=False)

