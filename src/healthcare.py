
from coordenadas import *
from collections import namedtuple
import csv
HealthCenter=namedtuple("HealthCenter",["nombre localidad coord estado num_camas disca uci"])
Coordinates=namedtuple("Coordinates","latitude, longitude")

def lee_centros(file):
    with open(file) as f:
        lista_out=[]
        reader=csv.reader(f)
        for nombre, localidad,latitud,longitud, estado,num_camas,tiene_acceso_disc,tiene_uci in reader:
            latitud=float(latitud)
            longitud=float(longitud)
            num_camas=int(num_camas)
            coord=Coordinates(latitud, longitud)
            tiene_acceso_disc=lambda x:True if tiene_acceso_disc=="true" else False
            tiene_acceso_disc=lambda x:True if tiene_uci=="true" else False
            lista_out.append([nombre,localidad,coord,estado,num_camas,tiene_acceso_disc,tiene_uci])
def read_centers(filename):
    pass

def total_bed_accessible_centers(listt_centers):
    pass