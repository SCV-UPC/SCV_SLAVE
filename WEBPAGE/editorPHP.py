import cercaIP
import Pyro4
import os



IP_MASTER=cercaIP.cerca()

intro=['<html>\n', '\t<head>\n', '\n', "\t\t<meta name='viewport' content='width=device-width,initial-scale=1'>\n", '\t\t<title>JASPER</title>\n', '\n', '\t</head>\n', '</html>\n', '\n', '<?php\n', "echo 'Soporte web para el Sistema de control por voz';\n"]
final1=['?>\n']
intro2=['<FORM NAME="blink" Method=\'POST\'>\n']
final2=['</FORM>\n']


def boto_nou(button_name,veu):

	return [ '\t<p>\n', '\t\t<?php\n', '\t\techo \'<button name="%s">%s</button>\';\n'%(button_name,veu), '\t\t?>\n', '\t</p>\n']

def comanda_nova(comanda,IP_MASTER,button):

	return ['if (isset($_POST[\'%s\'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py %s %s");}\n'%(button,"'"+comanda.strip()+"'","'"+IP_MASTER+"'")]

def trobar_comandes():

	comandesGlobals=Pyro4.Proxy("PYRO:jasper.comandesGlobals@%s:5164"%(IP_MASTER))
	return comandesGlobals.valor_actual()

def actualitzaPHP():

	os.system('sudo /etc/init.d/apache2 stop')

	diccionari=trobar_comandes()
	veu=[]
	comandes=[]
	IPs=[]
	botons=[]
	fitxer=intro
	for idx,paraules in enumerate(diccionari.keys()):
		veu.append(paraules)	
		comandes.append(diccionari[paraules][0])
		IPs.append(diccionari[paraules][1])
		botons.append("button%s"%(idx))

	for idx in range(len(comandes)):
		fitxer=fitxer+comanda_nova(comandes[idx],IPs[idx],botons[idx])
	fitxer=fitxer+final1
	for idx in range(len(botons)):
		fitxer=fitxer+intro2		
		fitxer=fitxer+boto_nou(botons[idx],veu[idx])
	fitxer=fitxer+final2
		
	f=open('/home/pi/SCV/WEBPAGE/jasper.php','w')
	text=''
	for el in fitxer:
		text=text+el
	f.write(text)
	f.close()

	os.system('sudo /etc/init.d/apache2 start')

if __name__=="__main__":

	actualitzaPHP()


