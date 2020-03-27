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
        print("Fallo "+cont)
        continue
else:
    print("No hay servidores disponibles, verifique su conexion a internet e intente más tarde")
    exit()
print ("hora de inicio de la petición = %s" %t1.time())
t2=datetime.datetime.now()

t1 = datetime.datetime.now()
print ("Fecha y hora = %s" % t1)
