import pandas as pd
import os

class interest():

    def exec(self):

        variables, need = self.enter()
        inversion, percent, period, time = self.pure_enter(variables)
        calculate = calculator(inversion, percent, period, time)
        acumulate, earning = calculate.interest_simple() if need == "1" else calculate.interest_compound()
        table = calculate.table_simple() if need == "1" else calculate.table_compound()
        line_1 = f"Acumulado: A = C*P*(n*t)\n\nA = {acumulate}\n\n" if need == "1" else f"\nAcumulado: A = C(1+P)^(nt)\n\nA = {acumulate}\n\n"

        self.clear_screen()

        print(line_1 +\
                f"Ganancia: G = A-P\n\nG = {earning}\n\n"\
                f"Intereses por periodo:\n\n{table}\n")

        self.clear_screen(True)

    def enter(self):

        type_interest = input("\nTipo de interes a calcular:\n\n"\
                                "1. Interes Simple\n"\
                                "2. Interes Compuesto\n\n"\
                                "Opcion: ")
        
        self.clear_screen()

        interest_needed = self.pure_type(type_interest)

        inversion = input("Inversion(C): ")
        percent = input("Porcentaje(P): ")
        time = input("Tiempo(t): ")
        period = input("Periodos(n): ")
        variables = [inversion, percent, period, time]

        return variables, interest_needed

    def pure_type(self, type_of_interest):

        if type_of_interest in ["1", "2"]:

            return type_of_interest

        else:

            print("Parametros incorrectos, ingreselos como se le indica")
            self.clear_screen(True)
            self.exec()
    
    def pure_enter(self, variables):

        for values in variables:

            validate = [sym not in values for sym in [",","."]]
            variables[variables.index(values)] = int(values) if all(validate) else float(values)

        inversion = variables[0]
        percent = variables[1]/100
        period = variables[2]
        time = variables[3]

        return inversion, percent, period, time

    def clear_screen(self, wait = False):

        if wait == True:

            os.system("pause")
        
        if os.name == "nt":

            os.system("cls")

        else:

            os.system("clear")

class calculator():

    def __init__(self, inversion, percent, period, time):

        self.inversion = inversion
        self.percent = percent
        self.period = period
        self.time = time

    def interest_simple(self):

        acumulated = self.inversion * (1 + self.percent) * (self.period*self.time)
        earning = acumulated - self.inversion

        return acumulated, earning

    def interest_compound(self):

        acumulated = self.inversion * ((1 + self.percent) ** (self.period * self.time))
        earning = acumulated - self.inversion

        return acumulated, earning

    def table_simple(self):

        inv_time = self.inversion
        values = self.inversion*self.percent
        rises = [self.inversion]
        length = [f"{per + 1} period" for per in range((self.period*self.time) + 1)]

        for times in range(self.period*self.time):

            inv_time += values
            rises.append(inv_time)

        percent_list = [f"{self.percent*100} %" for times in range(len(rises)-1)]
        percent_list.append(0)
        values_rised = [values for times in range(len(rises)-1)]
        values_rised.append(0)

        print(len(length), len(rises), len(values_rised), len(percent_list))

        data = {"Interes": rises,
                "Porcentaje": percent_list,
                "Aumento": values_rised}

        table_int_simple = pd.DataFrame(data, index=length)

        return table_int_simple

    def table_compound(self):

        inv_time = self.inversion
        values_rised = []
        rises = [self.inversion]
        length = [f"{per + 1} period" for per in range((self.period*self.time) + 1)]

        for times in range(self.period*self.time):

            values = inv_time*self.percent
            inv_time += values
            values_rised.append(values)
            rises.append(inv_time)

        percent_list = [f"{self.percent*100} %" for times in range(len(rises)-1)]
        values_rised.append(0)
        percent_list.append(0)

        data = {"Interes": rises,
                "Porcentaje": percent_list,
                "Aumento": values_rised}

        table_int_acum = pd.DataFrame(data, index=length)

        return table_int_acum

interest().exec()