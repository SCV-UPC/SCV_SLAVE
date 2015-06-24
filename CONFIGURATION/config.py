import Pyro4
import cercaIP
IP=cercaIP.cerca()

def config():

	l=[]

	f=open('/home/pi/SCV/CONFIGURATION/config.txt','r')
	for idx,linia in enumerate(f.readlines()):

		linia=linia.strip()
		linia= linia.split('*')

		if idx<8:

			try:

				l.append(linia[1])

			except:
			
				l.append('Error')

		else:

			return l
	return l


class Config():

	def __init__(self):

		self.config=config()

	def actualitza(self):

		self.config=config()

Config=Config()
"""
nom*MASTER
app_key AT&T*akgpcgksgua9ak6coo2gbsmcipbw4tza
app_secret AT&T*q7m0gegmnh6aidcycvkgalczhp1m6d5y
token WITAI en angles*62Z4YOLS4ULORUBITFVT7WO6DJULX2ZV
token WITAI en castella*AHWDLGI7GWULZLVKKTTX5FOADV74THYV
key Google*AIzaSyDgU56QeumsMHrJ6kP7xXOMCM8hFOKZp6U
motor STT a usar*attC
paraula clau*JASPER
"""

class Config_slave():

	def valor_actual(self):

		return Config.config

	def actualitza(self):

		Config.actualitza()

config_slave=Config_slave()	
Pyro4.Daemon.serveSimple({config_slave:"jasper.Config"},port=5111,host=IP,ns=False)

		
