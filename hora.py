#Importacion
import datetime
import ntplib
import os
from time import ctime

#Comunicacion con el servidor
cont=1
servidor_de_tiempo= "time.nist.gov ","time.windows.com","time-a-b.nist.gov ","utcnist.colorado.edu ","time-a-g.nist.gov","time-c-wwv.nist.gov"
for i in servidor_de_tiempo:
    try:
        t1=datetime.datetime.now()
        cliente_ntp = ntplib.NTPClient()
        respuesta = cliente_ntp.request(i)
        print("Se usara %s para obtener la fecha y hora\n" %i)
        cont+=1
        break
    except:
        print("Fallo %s" %cont)
        continue
else:
    print("No hay servidores disponibles, verifique su conexion a internet e intente más tarde")
    exit()

t2=datetime.datetime.now()
petdelay= datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
indelay=(t2-t1)/2
delay=petdelay+indelay
print ("hora de inicio de la petición = %s" %t1.time())
print ("hora de llegada de la petición = %s " %t2.time())
print ("Fecha/hora que se recibió del servidor de tiempo =%s " %petdelay)
print ("tiempo de retraso del paquete = %s " %indelay)
print ("hora/fecha que se va a cambiar en la computadora local= %s " %delay)

try:
    os.system('date --set "%s"' %delay)
    os.system('hwclock --set --date="%s"' %delay)
except:
    print("\n\nHa ocurrido un error\n\n")
    exit("Recuerde iniciar este programa con root")
print("\n\nLa fecha se ha cambiado exitosamente.")