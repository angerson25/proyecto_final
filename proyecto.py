#Importarla libreria tkinter y todas sus funciones
from tkinter import *
from tkinter import Tk, Label, Button, Entry, Spinbox, OptionMenu, StringVar, Toplevel

#-----------------
#Ventana principal
#-----------------

#funciones
#funcion piernas
def dieta():
    ventana_dieta = Toplevel()
    ventana_dieta.title("Dieta")
    ventana_dieta.resizable(False, False)
    imagen=PhotoImage(file="dietafondo.png")
    fondo=Label(ventana_dieta, image=imagen)
    fondo.place(x=0,y=0)
    ventana_dieta.geometry("600x600")
    ventana_dieta.mainloop()
def piernas():
    ventana_piernas = Toplevel()
    ventana_piernas.title("Piernas")
    ventana_piernas.resizable(False, False)
    imagen=PhotoImage(file="piernas.png")
    fondo=Label(ventana_piernas, image=imagen)
    fondo.place(x=0,y=0)
    ventana_piernas.geometry("884x482")
    ventana_piernas.mainloop()

def brazos():
    ventana_brazos = Toplevel()
    ventana_brazos.title("Brazos")
    ventana_brazos.resizable(False, False)
    imagen=PhotoImage(file="brazos.png")
    fondo=Label(ventana_brazos, image=imagen)
    fondo.place(x=0,y=0)
    ventana_brazos.geometry("884x482")
    ventana_brazos.mainloop()


def abdomen():
    ventana_abdomen = Toplevel()
    ventana_abdomen.title("Abdomen")
    ventana_abdomen.resizable(False, False)
    imagen=PhotoImage(file="abdomen.png")
    fondo=Label(ventana_abdomen, image=imagen)
    fondo.place(x=0,y=0)
    ventana_abdomen.geometry("884x482")
    ventana_abdomen.mainloop()

def cardio():
    ventana_cardio = Toplevel()
    ventana_cardio.title("cardio")
    ventana_cardio.resizable(False, False)
    imagen=PhotoImage(file="cardio.png")
    fondo=Label(ventana_cardio, image=imagen)
    fondo.place(x=0,y=0)
    ventana_cardio.geometry("884x482")
    ventana_cardio.mainloop()

#Se declara una variable llamada ventana_principal y que adquiere las caracteristicas tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Proyecto")

#dimensiones de la ventana(ancho,alto)
ventana_principal.geometry("884x482")

#permite deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondo
ventana_principal.config(bg="white")

#imagen de fondo
imagenfondo=PhotoImage(file="fondo.png")
fondo_principal=Label(ventana_principal, image=imagenfondo)
fondo_principal.place(x=0,y=0)

#boton
imagepiernas=PhotoImage(file="ejepiernas.png")
bt_pie = Button(fondo_principal,image=imagepiernas, command=piernas)
bt_pie.place(x=50, y=200, width=171, height=120)

#boton
imagenbrazos=PhotoImage(file="ejebrazos.png")
bt_pie = Button(fondo_principal,image=imagenbrazos , command=brazos)
bt_pie.place(x=246, y=200, width=171, height=120)

#boton
imageabdomen=PhotoImage(file="ejeabdomen.png")
bt_ab = Button(fondo_principal, image=imageabdomen , command=abdomen)
bt_ab.place(x=442, y=200, width=171, height=120)

#boton
imagencardeo=PhotoImage(file="ejecardio.png")
bt_ab = Button(fondo_principal,image=imagencardeo , command=cardio)
bt_ab.place(x=638, y=200, width=171, height=120)

#boton
imagendieta=PhotoImage(file="dieta.png")
bt_ab = Button(fondo_principal,image=imagendieta,command=dieta)
bt_ab.place(x=638, y=380, width=120, height=80)






ventana_principal.mainloop()




