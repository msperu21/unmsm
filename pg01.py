# UNMSM - Programa RSU MentorTIC
# Taller de Algoritmos y Programación con Python - PG01
# Caso: Estrategia de Negocio Nikken Challenge
""" Comprende la comercialización de 4 sistemas de agua pura, alcalina, mineralizada y antioxidante, en dos grupos: Básico (Pi Water) y Avanzado (Waterfall, aqua pour y pimag optimizer) """
# pg01.py: Determinar la ganancia mensual de un Asesor, considerando un máximo de venta de 7 equipos Waterfall, durante 6 meses.

import random  # Módulo (Library) para generar nros aleatorios
KINYA = 3  # Convención para definir constantes
MAXVENTAS = 7   
MESES = 6
# Asesores comercializan equipos
Asesor = "Kimberly" # Variable tipo string/cadena
eqavz_dn = "Waterfall" # Denominación del equipo
eqavz_pr = 1720  # Variable entera. Precio en soles
# Ganancia inmediata x c/u (Comisión por venta)
eqavz_gi = 293 # Ganancia inmediata
eqavz_b1 = 140 # Bono Kinya! x c/u, si vende al menos 3 x mes
iter = 0  # Contador de las iteraciones
print("Resultados del Asesor:", Asesor)
print("Por ventas de equipos:", eqavz_dn)
print("Mes Vtas G.I.  B1  Ganancia")
gTotal = 0 # Acumulador de la ganancia total
while iter < MESES:
  # Genera en forma aleatoria un entero entre 0 y 7
  nrVentas = random.randint(0, MAXVENTAS)
  gi = nrVentas * eqavz_gi  # Ganancia inmediata
  nrKinya = int(nrVentas/KINYA)
  if nrKinya > 0:   
    b1 = nrKinya * (eqavz_b1 * KINYA) # Ganancia x bono Kinya!
    b1 = b1 + (nrVentas - (nrKinya * KINYA))  * eqavz_b1
  else:
    b1=0
  gMes = gi + b1 # Ganancia del mes
  gTotal += gMes # Ganancia total
  print('{:2}'.format(iter+1),'{:3}'.format(nrVentas), '{:5}'.format(gi), '{:4}'.format(b1), '{:7}'.format(gMes))
  iter = iter + 1 # Fin de loop / lazo

print("=========================")
print('{:25}'.format(gTotal))