import Pyro4
import sys

IP_MASTER=sys.argv[1]
simulador=Pyro4.Proxy("PYRO:jasper.Simulador@%s:5123"%(IP_MASTER))

try:
	llista=simulador.valor_actual()
	llista[31]=1
	llista[32]=1
	simulador.modifica_estat(llista)

except:

	pass
