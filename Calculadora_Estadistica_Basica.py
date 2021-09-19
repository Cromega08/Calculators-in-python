import numpy as np
from numpy.core.fromnumeric import size
from scipy import stats
import re



enter_data = input("Ingrese los datos separados por espacios o comas (' ', ','),\n"\
                    "los valores decimales señalados por puntos ('.')\n"\
                    "y evite los caracteres alfabeticos diferentes a los indicados antes\n\n"\
                    "Datos: ")

class data():

    def 

data_pure = re.sub("[a-zA-Z]|,", "", enter_data.strip())
data_str = re.split(" ", data_pure)
data = np.array(data_str).astype(np.float_)
data.sort()
mean = data.mean()
indexs = np.array([np.round(data.size/2, 0) - 1, np.round(data.size/2, 0) - 1, np.round(data.size/2, 0)]).astype(np.int_)
mid = data[indexs[0]] if data.size%2 != 0 else (data[indexs[1]] + data[indexs[2]])/2

mod = stats.mode(data)

print(f"\nDatos: {data}\n"\
    f"Tamaño: {data.size} datos\n"
    f"Media: {mean}\n"\
    f"Mediana: {mid}\n"\
    f"Moda: Valor = {np.round(mod.mode[0])} ; Frecuencia = {mod.count[0]}\n")