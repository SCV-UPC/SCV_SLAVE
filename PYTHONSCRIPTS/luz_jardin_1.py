import Pyro4
import sys

IP_MASTER=sys.argv[1]
simulador=Pyro4.Proxy("PYRO:jasper.Simulador@%s:5123"%(IP_MASTER))

try:
	llista=simulador.valor_actual()
	llista[24]=1
	llista[25]=1
	llista[26]=1
	llista[27]=1
	simulador.modifica_estat(llista)

except:

	pass
