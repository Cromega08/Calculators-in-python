inv = input("Inversion: ")
per = input("Porcentaje: ")
peri = input("Periodos: ")
time = input("Tiempo: ")
var = [inv, per, peri, time]

for values in var:

    validate = [sym not in values for sym in [",","."]]
    var[var.index(values)] = int(values) if all(validate) else float(values)

inv = var[0]
per = var[1]/100
peri = var[2]
time = var[3]

acum = inv*((1+per)**(peri*time))

print(f"\nAcumulado: A = P(1+n)^(nt)\n\nA = {round(acum, 2)}\n")
print(f"Ganancia: G = A-P\n\nG = {round(acum-inv, 2)}\n")

for times in range(int(peri*time)):

    inv += inv*per
    print (round(inv, 2))