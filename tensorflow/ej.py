import numpy as np
import tkinter as tk
from tkinter import ttk
import tensorflow as tf
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

# Datos de entrada
años = np.array([1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
consumos = np.array([126.56, 128.53, 132.66, 138.75, 147.05, 151.21, 154.75, 156.69, 155.46, 160.90, 165.60, 173.37, 189.14, 193.39, 205.63, 220.92, 233.07, 239.91, 257.30, 273.65, 284.46, 295.26, 301.53, 310.67, 291.53, 298.15, 291.37, 293.77, 281.47, 274.94, 277.48, 271.19, 272.90])

# Crear y entrenar un modelo de regresión con TensorFlow
model_tf = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=(1,))
])
model_tf.compile(optimizer='adam', loss='mean_squared_error')
model_tf.fit(años, consumos, epochs=1000, verbose=0)

# Función para predecir el consumo utilizando TensorFlow
def predecir_consumo_tensorflow():
    año_a_predecir = float(entry_año.get())
    consumo_predicho = model_tf.predict([año_a_predecir])
    label_resultado.config(text=f"Consumo estimado (TensorFlow): {consumo_predicho[0][0]:.2f}")


    # Crear un gráfico de dispersión de los datos reales
    plt.figure(figsize=(8, 4))
    plt.scatter(años, consumos, label="Datos reales", color='b')
    
    # Agregar la predicción al gráfico
    plt.scatter(año_a_predecir, consumo_predicho[0][0], label="Predicción", color='r')
    
    # Configuración del gráfico
    plt.xlabel('Año')
    plt.ylabel('Consumo eléctrico')
    plt.title('Predicción de Consumo Eléctrico')
    plt.legend()
    plt.grid(True)

    # Mostrar el gráfico
    plt.show()
    
# Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title("Predicción de Consumo Eléctrico")
ventana.geometry("400x400")

##################################################################
# Crear un Treeview (tabla)
#tabla = ttk.Treeview(ventana, columns=("Año", "Consumo electrico"))
## Definir las columnas
#tabla.heading("#1", text="Nombre")
#tabla.heading("#2", text="Edad")
# Configurar el ancho de las columnas
#tabla.column("#1", width=50)
#tabla.column("#2", width=50)
# Insertar datos en la tabla (datos ficticios)
#tabla.insert("", "end", values=("Juan", 30))
#tabla.insert("", "end", values=("María", 25))
#tabla.insert("", "end", values=("Carlos", 35))
#tabla.insert("", "end", values=("Luisa", 28,))
##################################################################

# Crear elementos de la interfaz
label_año = tk.Label(ventana, text="Año de consumo a predecir:")
entry_año = tk.Entry(ventana)
boton_predecir_tensorflow = tk.Button(ventana, text="Predecir (TensorFlow)", command=predecir_consumo_tensorflow)
label_resultado = tk.Label(ventana, text="")
label_imagen = tk.Label(ventana)

# Cargar una imagen para mostrar
imagen = Image.open("C:/xampp/htdocs/tensorflow/tensorflow/tensorflow/static/imgs/lineas.jpg")
imagen = imagen.resize((400, 200), Image.ANTIALIAS)
imagen = ImageTk.PhotoImage(imagen)
label_imagen.config(image=imagen)
label_imagen.image = imagen

# Colocar elementos en la ventana
label_imagen.pack()
label_año.pack()
entry_año.pack()
boton_predecir_tensorflow.pack()
label_resultado.pack()
#tabla.pack()

# Iniciar la ventana
ventana.mainloop()

