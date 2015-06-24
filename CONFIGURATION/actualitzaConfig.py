import Pyro4
import cercaIP

Config=Pyro4.Proxy("PYRO:jasper.Config@%s:5111"%(cercaIP.cerca()))
Config.actualitza()

