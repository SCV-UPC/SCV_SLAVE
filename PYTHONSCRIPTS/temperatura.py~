#executaComandes.executa("%s '%s' '%s' '%s' '%s' &"%(linia,IP_MASTER,IP,num_mic,text))
import Pyro4
import sys
import adaptar
import escolta
import parla

IP_MASTER=sys.argv[1]
IP=sys.argv[2]
num_mic=sys.argv[3]
text=sys.argv[4]


comandesGlobals=Pyro4.Proxy("PYRO:jasper.comandesGlobals@%s:5164"%(IP_MASTER))
simulador=Pyro4.Proxy("PYRO:jasper.Simulador@%s:5123"%(IP_MASTER))

try:
	
	comandesGlobals.modifica_ocupat(1)#deshabilitar l'altre proces de deteccio de veu Jasper2
	parla.parla(IP,num_mic,'Dime la temperatura, porfavor.')
	temp=escolta.escolta(IP,num_mic)
	print temp
	temp=adaptar.adaptar(temp[0])
	print temp

	temp=int(temp)
	
	temp=str(temp)

	if len(temp)==1:
		temp='0'+temp

	s='%s graus'%(temp)
	simulador.modifica_temperatura(s)

	print s


except:

	mic.parla_0("Error. Solo numeros porfavor.")

	comandesGlobals.modifica_ocupat(0)#habilitar Jasper2


comandesGlobals.modifica_ocupat(0)#habilitar Jasper2
