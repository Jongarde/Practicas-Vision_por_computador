import cv2
import numpy as np
import tkinter as tk
from tkinter import Scale

# Función para actualizar los valores cuando los controles deslizantes cambian
def update_values():
    global limite_bajo, limite_alto, gauss, xy
    limite_bajo = limite_bajo_slider.get()
    limite_alto = limite_alto_slider.get()
    gauss = gauss_slider.get()
    xy = xy_slider.get()

    # Asegurarse de que el valor de gauss sea impar
    gauss = max(1, gauss) if gauss % 2 == 0 else gauss

    # Procesar la imagen con los nuevos valores
    process_image()

# Función para procesar la imagen con los valores actuales
def process_image():
    img = cv2.pyrDown(cv2.imread("gorka.jpeg", cv2.IMREAD_UNCHANGED))
    img = cv2.resize(img, (600, 600))

    blurred = cv2.GaussianBlur(img, (gauss, gauss), xy, xy)
    mask = cv2.inRange(cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY), limite_bajo, limite_alto)

    frame = cv2.bitwise_and(img, img, mask=mask)

    # Mostrar la imagen en una ventana
    cv2.imshow("hull", frame)
    cv2.waitKey(1)

# Crear la ventana de control
root = tk.Tk()
root.title("Control de Parámetros")

# Crear controles deslizantes para ajustar los valores
limite_bajo_slider = Scale(root, label="Limite Bajo", from_=0, to=255, orient="horizontal", length=300)
limite_alto_slider = Scale(root, label="Limite Alto", from_=0, to=255, orient="horizontal", length=300)
gauss_slider = Scale(root, label="Gauss", from_=1, to=81, orient="horizontal", length=300, resolution=1)
xy_slider = Scale(root, label="xy", from_=1, to=51, orient="horizontal", length=300, resolution=2)

limite_bajo_slider.pack()
limite_alto_slider.pack()
gauss_slider.pack()
xy_slider.pack()

# Configurar una función de actualización para los controles deslizantes
limite_bajo_slider.bind("<Motion>", lambda event: update_values())
limite_alto_slider.bind("<Motion>", lambda event: update_values())
gauss_slider.bind("<Motion>", lambda event: update_values())
xy_slider.bind("<Motion>", lambda event: update_values())

# Establecer los valores iniciales
limite_bajo = 60
limite_alto = 130
gauss = 11
xy = 25

limite_bajo_slider.set(limite_bajo)
limite_alto_slider.set(limite_alto)
gauss_slider.set(gauss)
xy_slider.set(xy)

# Procesar la imagen inicial
process_image()

# Iniciar el bucle principal de la ventana
root.mainloop()

# Limpiar después de cerrar la ventana
cv2.destroyAllWindows()