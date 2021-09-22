from pathlib import Path as p
from google_trans_new import google_translator as translator
from os import name, system
from sys import exit
import re

class app():

    def __init__(self):

       self.calculators_available = self.select()

    def exec(self):
        
        for calculators in self.calculators_available:

            print(f"{self.calculators_available.index(calculators) + 1}. {calculators}")
        
        out = len(self.calculators_available) + 1

        print(f"{out}. Salir")
        choice = input("Opcion: ")
        action = self.pure_choice(choice)

        self.clear_screen()

        if action == str(out):

            exit()

        elif action == "1":

            from calculators.frequency_table import table

            table().exec()

        elif action == "2":

            from calculators.interests import interest

            interest().exec()

        elif action == "3":

            from calculators.mean_median_mode import statistic

            statistic().exec()

        self.exec()
    
    def select(self):

        calculators_dir = p.cwd().joinpath("calculators")
        calculators_created = [re.sub(".py|_", " ", files.name).strip() for files in p(calculators_dir).iterdir()]
        
        for names in calculators_created:

            if "cache" in str(names):

                calculators_created.remove(names)
            

        translates = translator().translate("~".join(calculators_created), "es", "en")
        calculators_translated = translates.title().split(" ~ ")
        
        return calculators_translated

    def pure_choice(self, choice):

        if choice.isnumeric() and int(choice) in range(1, len(self.calculators_available) + 2): 

            return choice

        else:

            print("Parametros incorrectos, por favor indiquelos como se les indica")
            self.exec()

    def clear_screen(self):

        if name == "nt":

            system("cls")
        
        else:

            system("clear")