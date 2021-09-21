import numpy as np
from numpy.core.fromnumeric import size
from scipy import stats
import re
import os

class estadistic():

    def exec(self):

        enter_data = input("Ingrese los datos separados por espacios o comas (' ', ','),\n"\
                    "los valores decimales señalados por puntos ('.')\n"\
                    "y evite los caracteres alfabeticos diferentes a los indicados antes\n\n"\
                    "Datos: ")

        self.clear_screen()
        
        data_pured = data().pure_data(enter_data)
        mean, mid, mod = data().calculate(data_pured)

        print(f"\nDatos: {data_pured}\n"\
                f"Tamaño: {data_pured.size} datos\n"
                f"Media: {mean}\n"\
                f"Mediana: {mid}\n"\
                f"Moda: Valor = {np.round(mod.mode[0])} ; Frecuencia = {mod.count[0]}\n")

        self.clear_screen(True)

    def clear_screen(self, wait = False):

        if wait == True:

            os.system("pause")
        
        if os.name == "nt":

            os.system("cls")
        
        else:

            os.system("clear")

class data():

    def pure_data(self, enter_data):

        data_pure = re.sub("[a-zA-Z]|,", "", enter_data.strip())
        data_str = re.split(" ", data_pure)
        data = np.array(data_str).astype(np.float_)
        data.sort()

        return data
    
    def calculate(self, data):

        indexs = np.array([np.round(data.size/2, 0) - 1, np.round(data.size/2, 0) - 1, np.round(data.size/2, 0)]).astype(np.int_)
        mean = data.mean()
        mid = data[indexs[0]] if data.size%2 != 0 else (data[indexs[1]] + data[indexs[2]])/2
        mod = stats.mode(data)

        return mean, mid, mod