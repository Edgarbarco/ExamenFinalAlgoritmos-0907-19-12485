#El propietario del predio "Mega Autos" necesita ayuda con un sistema facil de utilizar para ayudarle a mejorar la administracion de su negocio. 
#Por lo tanto le ha solicitado su ayuda como un prometedor Ing. en sistemas en crearle una aplicacion con las siguientes caracteristicas:

import tkinter as tk
from tkinter import messagebox

class vehiculo:
    def __init__ (self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

def agregar_vehiculo():
    marca = entry_marca.get()
    modelo = entry_modelo.get()

    if marca and modelo:
        vehiculo = vehiculo(marca, modelo)
        lista_vehiculo.append(vehiculo)
        actualizar_lista()
        limoiar_entradas()
    else: 
        messagebox.showwarning("Advertencia, por favor completar todos los campos.")

def editar_vehiculo():
    seleccion =  lista_vehiculobox.curselection()

    if seleccion:
        indice = seleccion[0]
        vehiculo = lista_vehiculo[indice]
        nueva_marca = entry_marca.get()
        nuevo_modelo = entry_modelo.get()

    if nueva_marca and nuevo_modelo:
        vehiculo.marca = nueva_marca
        vehiculo.modelo = nuevo_modelo
        actualizar_lista()
        limpiar_entrada()
    else:
        messagebox.showwarning("Advertencia, por favor completar todos los campos.")

    else:
        messagebox.showwarning("Advertencia, Seleccionar un vehiculo para editar.")
    
def actualizar_lista():
    seleccion = lista_vehiculobox.curselection()

    if seleccion[0]
    lista_vehiculo.pop(indice)
    actualizar_lista()
    limpiar_entrada()

else: 
    messagebox.showwarning("Advertencia, selecciona un vehiculo para eliminar.")

def actualizar_lista():
    lista_vehiculobox.delete(0, tk.END)
    for vehiculo in lista_vehiculo:
        lista_vehiculobox.insert(tk.END, f{vehiculo.marca} - {vehiculo.modelo}"")

def limpiar_entrada():
    entry_marca.delete(0, tk.END)
    entry_modelo.delete(0, tk.END)

ventana = tk.tk()
ventana.title("Gestion de vehiculo")

lista_vehiculo = []

label_marca = tk.label(ventana, text = "marca")
label_marca.grid(row=0, column=0 sticky="E")

entry_marca = tk.Entry(ventana)
entry_marca.grid(row=0 , column=1)

label_modelo = tk.label(ventana, text = "modelo")
label_modelo.grid(row=0, column=0 sticky="E")

entry_modelo = tk.Entry(ventana)
entry_modelo.grid(row=0 , column=1)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_vehiculo)
boton_agregar.grid(row=2, column=0, columnspan=2, pady=10)

boton_editar = tk.Button(ventana, text="Editar", command=Editar_vehiculo)
boton_editar.grid(row=2, column=0, columnspan=2, pady=10)

boton_eliminar = tk.Button(ventana, text="Eliminar", command=Eliminar_vehiculo)
boto_eliminar.grid(row=2 , column=0, columnspan=2, pady=10)
