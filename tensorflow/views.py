from django.shortcuts import render
import numpy as np
from sklearn.linear_model import LinearRegression

def index(request):
    consumo = '' 

    if request.method == 'POST':
        año_a_predecir = request.POST.get('año_a_predecir')

        if año_a_predecir:
            try:
                año_a_predecir = int(año_a_predecir)

                #lista de años y de consumos
                años = np.array([1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
                consumos = np.array([126.56, 128.53, 132.66, 138.75, 147.05, 151.21, 154.75, 156.69, 155.46, 160.90, 165.60, 173.37, 189.14, 193.39, 205.63, 220.92, 233.07, 239.91, 257.30, 273.65, 284.46, 295.26, 301.53, 310.67, 291.53, 298.15, 291.37, 293.77, 281.47, 274.94, 277.48, 271.19, 272.90])

                # Crear un modelo de regresión lineal
                modelo = LinearRegression()
                modelo.fit(años.reshape(-1, 1), consumos)

                # Realizar la predicción
                consumo_predicho = modelo.predict(np.array([[año_a_predecir]]))

                # Actualizar el valor de 'consumo' con la predicción
                consumo = consumo_predicho[0]

            except ValueError:
                consumo = None

    return render(request, 'index.html', {'consumo': consumo})
