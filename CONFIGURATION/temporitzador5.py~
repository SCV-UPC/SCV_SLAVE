import Pyro4
import cercaIP 
import time

Config=Pyro4.Proxy("PYRO:jasper.Config@%s:5111"%(cercaIP.cerca()))

while(1):

	Config.actualitza()
	time.sleep(100)
