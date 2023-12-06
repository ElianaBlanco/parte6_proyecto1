from functools import reduce
import os
import random

class Juego:
    def __init__(self, mapa, inicio, final):
        self.mapa = mapa
        self.inicio = inicio
        self.final = final
        self.px, self.py = inicio

    # ... (otros métodos sin cambios)

    @staticmethod
    def convertir_a_matriz(laberinto):
        return list(map(list, laberinto.split('\n')))

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa, inicio, final = self.leer_mapa_aleatorio(path_a_mapas)
        super().__init__(mapa, inicio, final)

    def leer_mapa_aleatorio(self, path_a_mapas):
        archivos = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            datos = archivo.readlines()

            # Extraer las coordenadas de inicio y fin del archivo
            dimensiones = datos[0].split()
            filas, columnas = int(dimensiones[0]), int(dimensiones[1])
            inicio = tuple(map(int, datos[1].split()))
            final = tuple(map(int, datos[2].split()))

            # Extraer el mapa del archivo usando reduce
            mapa = reduce(lambda x, y: x + y.strip(), datos[3:], '')

        return self.convertir_a_matriz(mapa), inicio, final
