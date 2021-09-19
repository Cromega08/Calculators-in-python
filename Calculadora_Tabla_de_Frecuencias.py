import numpy as np
import pandas as pd
import re
import os

class table():

    def exec(self):

        enter_data = input("\nIngrese los datos separados por espacios o comas (' ', ','),\n"\
                    "los valores decimales señalados por puntos ('.')\n"\
                    "y evite introducir cualquier cosa que no represente un dato\n\n"\
                    "Datos: ")

        data_pured, data_original = data().data_pure(enter_data)
        data_to_table = list(data().calculate(data_pured))
        table_frec = data().create_table(data_to_table)

        self.clean_screen()

        print(f"\n{data_original}\n"\
                f"{table_frec}\n")

        self.clean_screen(True)
        
        copy = input("Desea:\n"\
                    "1. Guardar en el portapapeles"\
                    "2. Guardar en un archivo Excel"\
                    "3. Guardar en un archivo .csv"\
                    "4. Todas las anteriores"\
                    "5. No guardar")
        
        data().save_table(table_frec, copy)

        print("Proceso completado")

        self.clean_screen(True)
    
    def clean_screen(self, wait = False):

        if wait == True:

            os.system("pause")

        if os.name == "nt":

            os.system("cls")
        
        else:

            os.system("clear")

class data():

    def data_pure(self, init_data):

        data_str = re.sub("[^a-zA-Z0-9.\s]", "", init_data.strip())
        data_list = re.split(" ", data_str)
        data = np.array(data_list)
        data.sort()

        return data, data_str

    def calculate(self, data):

        values, frec_abs = np.unique(data, return_counts=True)
        frec_abs_aslist = frec_abs.tolist()
        frec_abs_acum = np.asarray([sum(frec_abs_aslist[:indexs]) + frec_abs_aslist[indexs] if indexs != 0 else frec_abs_aslist[0] for indexs in range(len(frec_abs_aslist))], dtype=object)
        frec_abs_acum_aslist = frec_abs_acum.tolist()
        frec_rel = frec_abs/sum(frec_abs_aslist)
        frec_rel_acum = frec_abs_acum/sum(frec_abs_aslist)
        per = frec_rel*100
        per_acum = frec_rel_acum*100

        return values, frec_abs, frec_abs_acum, frec_rel, frec_rel_acum, per, per_acum
    
    def create_table(self, n_data):

        data_to_df = {"Xi": n_data[0],
                        "fi": n_data[1],
                        "Fi": n_data[2],
                        "hi": n_data[3],
                        "Hi": n_data[4],
                        "%": n_data[5],
                        "Σ %": n_data[6]}
                        
        frec_table = pd.DataFrame(data_to_df)
        
        return frec_table

    def save_table(self, table, option):

        if option == "1" or option == "4":

            table.to_clipboard()
            
        if option == "2" or option == "4":

            table.to_excel()

        if option == "3" or option == "4":

            table.to_csv()