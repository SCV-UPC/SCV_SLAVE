import time
import Pyro4
import cercaIP
from actualitzaCercaRaspberrys import cerca

IP=cercaIP.cerca()

class cercaRaspberrys():

	def __init__(self):

		self.IPs=cerca()

	def modifica(self,variable):

		self.IPs=variable

	def direccions(self):

		return self.IPs

cercaRaspberrys=cercaRaspberrys()
Pyro4.Daemon.serveSimple({cercaRaspberrys:"jasper.cercaRaspberrys"},port=5168,host=IP,ns=False)






