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
comandesGlobals.modifica_ocupat(0)#deshabilitar l'altre proces de deteccio de veu Jasper2
simulador=Pyro4.Proxy("PYRO:jasper.Simulador@%s:5123"%(IP_MASTER))

try:

	parla.parla(IP,num_mic,'Dime la hora, porfavor')

	hora=escolta.escolta(IP,num_mic)
	hora=adaptar.adaptar(hora[0])
	print hora

	parla.parla(IP,num_mic,'Dime los minutos, porfavor')

	minuts=escolta.escolta(IP,num_mic)
	minuts=adaptar.adaptar(minuts[0])
	print minuts

	hora=int(hora)
	minuts=int(minuts)
	
	hora=str(hora)
	minuts=str(minuts)

	if len(hora)==1:
		hora='0'+hora
	if len(minuts)==1:
		hora='0'+minuts

	s='%s:%s'%(hora,minuts)
	simulador.modifica_alarma(s)

	print s


except:

	mic.parla_0("Error. Solo numeros porfavor.")

	comandesGlobals.modifica_ocupat(0)#habilitar Jasper2


comandesGlobals.modifica_ocupat(0)#habilitar Jasper2
