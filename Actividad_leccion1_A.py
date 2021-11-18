import pandas as pd
import matplotlib.pyplot as plt


def minimo(l):
    min = 1000000000
    for i in l:
        if i<min:
            min = i
    return min

def maximo(l):
    max = -1000000000
    for i in l:
        if i>max:
            max = i
    return max

def media(l):
    return sum(l)/len(l)


df = pd.read_csv("finanzas2020.csv", sep='\t')

if len(df.columns) == 12:  # Comprobación de que hay 12 columnas (1 por mes)

    col = df[['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
              'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']]

    for m in col:
        if len(df[m]) != 0:  # Comprobación de que las columnas no están vacías
            try:
                df[m] = pd.to_numeric(df[m], errors='raise')
            except ValueError:
                df[m] = pd.to_numeric(df[m], errors='coerce')
                df[m] = df[m].fillna(0).astype('int')
        else:
            print(f"En el mes {m} no hay datos.")

    suma_mes = df.sum()
    # print(suma_mes)

    gasto_meses = []
    ingreso_meses = []

    for m in col:
        try:
            gasto = 0
            ingreso = 0
            for i in range(len(df[m])):
                if df[m].iloc[i] < 0:
                    gasto += df[m].iloc[i]
                elif df[m].iloc[i] > 0:
                    ingreso += df[m].iloc[i]
            gasto_meses.append(gasto)
            ingreso_meses.append(ingreso)
        except:
            print('ERROR')

    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
             'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    gastos = {'Gastos': gasto_meses}
    ahorros = {'Ahorros': suma_mes}
    ingresos = {'Mes': meses, 'Ingresos': ingreso_meses}
    df_gastos = pd.DataFrame(gastos, index=meses)
    df_ahorros = pd.DataFrame(ahorros, index=meses)
    df_ingresos = pd.DataFrame(ingresos).set_index('Mes')
    print("El mes y el importe del gasto más elevado del año, ha sido:",
          df_gastos.idxmin(axis=0), minimo(gasto_meses))
    print("El mes y el importe del ahorro más elevado del año, ha sido:",
          df_ahorros.idxmax(axis=0), maximo(suma_mes))
    print("La media de gastos del año es:", media(gasto_meses))
    print("El gasto total del año es:", sum(gasto_meses))
    print("Los ingresos totales del año son:", sum(ingreso_meses))
