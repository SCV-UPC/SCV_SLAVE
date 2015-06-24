import sys
import Pyro4

comanda=sys.argv[1]
IP=sys.argv[2]

executaComandes=Pyro4.Proxy("PYRO:jasper.executaComanda@%s:5163"%(IP))
executaComandes.executa("%s '%s' '%s' '%s' '%s' &"%(comanda,IP,IP,0,'a'))#des de la pagina web nomes sexecutara en wit.ai i en castella, de moment
