tasa_dolar_hoy = 0,85
print("--- CONVERSOR DE EUROS A DÓLARES ---")
euros = float(input("Introduce la cantidad en Euros (€): "))
dolares = euros * tasa_dolar_hoy
print(f"{euros}€ equivalen a {round(dolares, 2)}$ dólares.")
