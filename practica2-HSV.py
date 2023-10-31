import cv2
import numpy as np
import tkinter as tk
from tkinter import Scale

"""
# Initialize the camera capture
cap = cv2.VideoCapture(0)  # 0 indicates the default camera (usually the built-in webcam)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error capturing the video feed.")
        break

    #frame = cv2.resize(frame, (600, 600))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    limite_bajo = np.array([0, 30, 60], dtype=np.uint8)
    limite_alto = np.array([20, 180, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, limite_bajo, limite_alto)

    # Reduce noise with blur filters
    mask = cv2.medianBlur(mask, 5)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    skin = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Skin Detection', skin)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
"""

def update_values():
	global limite_bajo_h, limite_bajo_s, limite_bajo_v, limite_alto_h, limite_alto_s, limite_alto_h
	limite_bajo_h = limite_bajoh_slider.get()
	limite_bajo_s = limite_bajos_slider.get()
	limite_bajo_v = limite_bajov_slider.get()
	
	limite_alto_h = limite_altoh_slider.get()
	limite_alto_s = limite_altos_slider.get()
	limite_alto_v = limite_altov_slider.get()
	
	process_image()
    
def process_image():
	img = cv2.imread("gorka.jpeg")

	img = cv2.resize(img, (600, 600))

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	limite_bajo = np.array([limite_bajo_h, limite_bajo_s, limite_bajo_v], dtype=np.uint8)
	limite_alto = np.array([limite_alto_h, limite_alto_s, limite_alto_v], dtype=np.uint8)

	mask = cv2.inRange(hsv, limite_bajo, limite_alto)

	# Reduce noise with blur filters
	mask = cv2.medianBlur(mask, 5)
	mask = cv2.GaussianBlur(mask, (5, 5), 0)

	skin = cv2.bitwise_and(img, img, mask=mask)

	cv2.imshow('Skin Detection', skin)
	cv2.waitKey(1)

root = tk.Tk()
root.title("Control de Parámetros")

# Crear controles deslizantes para ajustar los valores
limite_bajoh_slider = Scale(root, label="Limite Bajo H", from_=0, to=360, orient="horizontal", length=300)
limite_bajos_slider = Scale(root, label="Limite Bajo S", from_=0, to=255, orient="horizontal", length=300)
limite_bajov_slider = Scale(root, label="Limite Bajo V", from_=0, to=255, orient="horizontal", length=300)

limite_altoh_slider = Scale(root, label="Limite Alto H", from_=0, to=360, orient="horizontal", length=300)
limite_altos_slider = Scale(root, label="Limite Alto S", from_=0, to=255, orient="horizontal", length=300)
limite_altov_slider = Scale(root, label="Limite Alto V", from_=0, to=255, orient="horizontal", length=300)

limite_bajoh_slider.pack()
limite_bajos_slider.pack()
limite_bajov_slider.pack()

limite_altoh_slider.pack()
limite_altos_slider.pack()
limite_altov_slider.pack()

# Configurar una función de actualización para los controles deslizantes
limite_bajoh_slider.bind("<Motion>", lambda event: update_values())
limite_bajos_slider.bind("<Motion>", lambda event: update_values())
limite_bajov_slider.bind("<Motion>", lambda event: update_values())

limite_altoh_slider.bind("<Motion>", lambda event: update_values())
limite_altos_slider.bind("<Motion>", lambda event: update_values())
limite_altov_slider.bind("<Motion>", lambda event: update_values())

# Establecer los valores iniciales
limite_bajo_h = 0
limite_bajo_s = 91
limite_bajo_v = 84

limite_alto_h = 20
limite_alto_s = 180
limite_alto_v = 255

limite_bajoh_slider.set(limite_bajo_h)
limite_bajos_slider.set(limite_bajo_s)
limite_bajov_slider.set(limite_bajo_v)

limite_altoh_slider.set(limite_alto_h)
limite_altos_slider.set(limite_alto_s)
limite_altov_slider.set(limite_alto_v)

# Procesar la imagen inicial
process_image()

# Iniciar el bucle principal de la ventana
root.mainloop()

# Limpiar después de cerrar la ventana
cv2.destroyAllWindows()
