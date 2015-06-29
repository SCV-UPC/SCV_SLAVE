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

class Config_slave():

	def valor_actual(self):
		return Config.config

	def actualitza(self):
		Config.actualitza()

config_slave=Config_slave()	
Pyro4.Daemon.serveSimple({config_slave:"jasper.Config"},port=5111,host=IP,ns=False)

		
