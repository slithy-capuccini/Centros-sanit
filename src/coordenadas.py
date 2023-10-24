import math
def calcula_distancia(coord1,coord2):
    return math.sqrt((coord2.latitude-coord1.latitude)**2+(coord2.longitude-coord1.longitude)**2)
def avarage_coord(coords):
    #devuelve una cordenada que es la media de las longitudes y otra de las latitudes
    avr_latitudes=sum([i.latitude for i in coords])/len(coords)
    avr_longitudes=sum([i.longitude for i in coords])/len(coords)
    return avr_latitudes, avr_longitudes

