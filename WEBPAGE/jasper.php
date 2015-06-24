<html>
	<head>

		<meta name='viewport' content='width=device-width,initial-scale=1'>
		<title>JASPER</title>

	</head>
</html>

<?php
echo 'Soporte web para el Sistema de control por voz';
if (isset($_POST['button0'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/canal.py' '192.168.1.40'");}
if (isset($_POST['button1'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/luz_hab_principal_1.py' '192.168.1.40'");}
if (isset($_POST['button2'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/ventilador_1.py' '192.168.1.40'");}
if (isset($_POST['button3'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/puerta_salon_1.py' '192.168.1.40'");}
if (isset($_POST['button4'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/luz_hab_ninos_0.py' '192.168.1.40'");}
if (isset($_POST['button5'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/puerta_jardin_1.py' '192.168.1.40'");}
if (isset($_POST['button6'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/luz_hab_principal_0.py' '192.168.1.40'");}
if (isset($_POST['button7'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/ventilador_0.py' '192.168.1.40'");}
if (isset($_POST['button8'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/ventana_salon_0.py' '192.168.1.40'");}
if (isset($_POST['button9'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/luz_salon_0.py' '192.168.1.40'");}
if (isset($_POST['button10'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/luz_hab_ninos_1.py' '192.168.1.40'");}
if (isset($_POST['button11'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/ventana_cocina_0.py' '192.168.1.40'");}
if (isset($_POST['button12'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/luz_salon_1.py' '192.168.1.40'");}
if (isset($_POST['button13'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/televisor_0.py' '192.168.1.40'");}
if (isset($_POST['button14'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/alarma.py' '192.168.1.40'");}
if (isset($_POST['button15'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/puerta_salon_0.py' '192.168.1.40'");}
if (isset($_POST['button16'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/puerta_cocina_0.py' '192.168.1.40'");}
if (isset($_POST['button17'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/luz_cocina_0.py' '192.168.1.40'");}
if (isset($_POST['button18'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/ventana_hab_principal_0.py' '192.168.1.40'");}
if (isset($_POST['button19'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/ventana_cocina_1.py' '192.168.1.40'");}
if (isset($_POST['button20'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/puerta_jardin_0.py' '192.168.1.40'");}
if (isset($_POST['button21'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/temperatura.py' '192.168.1.40'");}
if (isset($_POST['button22'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/musica_salon_0.py' '192.168.1.40'");}
if (isset($_POST['button23'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/ventana_hab_principal_1.py' '192.168.1.40'");}
if (isset($_POST['button24'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/ventana_salon_1.py' '192.168.1.40'");}
if (isset($_POST['button25'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/televisor_1.py' '192.168.1.40'");}
if (isset($_POST['button26'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/puerta_cocina_1.py' '192.168.1.40'");}
if (isset($_POST['button27'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/musica_salon_1.py' '192.168.1.40'");}
if (isset($_POST['button28'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/luz_cocina_1.py' '192.168.1.40'");}
if (isset($_POST['button29'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/ventana_hab_ninos_0.py' '192.168.1.40'");}
if (isset($_POST['button30'])){shell_exec("python /home/pi/SCV/WEBPAGE/executaPHP.py 'python /home/pi/SCV/PYTHONSCRIPTS/ventana_hab_ninos_1.py' '192.168.1.40'");}
?>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button0">CANAL</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button1">ENCENDER LUZ HABITACION PRINCIPAL</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button2">ENCENDER VENTILADOR</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button3">CERRAR PUERTA SALON</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button4">APAGAR LUZ HABITACION NINOS</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button5">CERRAR PUERTA JARDIN</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button6">APAGAR LUZ HABITACION PRINCIPAL</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button7">APAGAR VENTILADOR</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button8">ABRIR VENTANA SALON</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button9">APAGAR LUZ SALON</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button10">ENCENDER LUZ HABITACION NINOS</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button11">ABRIR VENTANA COCINA</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button12">ENCENDER LUZ SALON</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button13">APAGAR TELEVISOR</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button14">ALARMA</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button15">ABRIR PUERTA SALON</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button16">ABRIR PUERTA COCINA</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button17">APAGAR LUZ COCINA</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button18">ABRIR VENTANA HABITACION PRINCIPAL</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button19">CERRAR VENTANA COCINA</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button20">ABRIR PUERTA JARDIN</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button21">TEMPERATURA</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button22">APAGAR MUSICA SALON</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button23">CERRAR VENTANA HABITACION PRINCIPAL</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button24">CERRAR VENTANA SALON</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button25">ENCENDER TELEVISOR</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button26">CERRAR PUERTA COCINA</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button27">PONER MUSICA SALON</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button28">ENCENDER LUZ COCINA</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button29">ABRIR VENTANA HABITACION NINOS</button>';
		?>
	</p>
<FORM NAME="blink" Method='POST'>
	<p>
		<?php
		echo '<button name="button30">CERRAR VENTANA HABITACION NINOS</button>';
		?>
	</p>
</FORM>
