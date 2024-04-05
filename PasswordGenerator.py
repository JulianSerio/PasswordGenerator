#Password generator
from tkinter import *
from tkinter import messagebox
import random
import tkinter 
import tkinter.ttk as ttk

#GENERATE 
def generatePassword():
    length = length.get()  # Obtener la longitud deseada de la contraseña
    options = ''

    # Construir las opciones de caracteres basadas en las selecciones del usuario
    if mayus.get():
        options += string.ascii_uppercase
    if minus.get():
        options += string.ascii_lowercase
    if numb.get():
        options += string.digits
    if simb.get():
        options += string.punctuation

    # Generar la contraseña aleatoria
    if options:
        password = ''.join(random.choices(options, k=length))
    else:
        # Si no se selecciona ninguna opción, usar todos los caracteres
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

    etiqueta = password.set(password)  # Mostrar la contraseña generada
    
#FUNCTION TO COPY
def copy(): 
    if (password.get() != ""): 
        ventana.clipboard_clear()
        ventana.clipboard_append(password.get())
        labelVar.set("Copiado!")
    else:
        messagebox.showwarning("Error!","Primero genere la contraseña")

#VENTANA CONFIG
ventana = tkinter.Tk()
ventana.title("Password Generator") 
ventana.geometry("500x300+675+300") 
ventana.resizable(width=False,height=False)
ventana.configure(bg="#FF5555")

#VARIABLES FOR DETECT WHO'S PRESSED
mayus = IntVar()
minus = IntVar()
numb = IntVar()
simb= IntVar()

#VARIABLES
length = IntVar()
password = StringVar()
labelVar = StringVar()

#LABELFRAME CONTAINER 
frame = LabelFrame(ventana,  padx=30, pady=50)
frame.pack(pady=20, padx=10)

#LABELS SHOW TEXT
label = Label(ventana, textvariable=labelVar,background="#FF5555",font="sanfrancisco").place(x=350,y=250)
label2 = Label(ventana, text="Longitud:" ).place(x=160,y=170)
etiqueta = Label(ventana, textvariable=password,font=60).place(x=200,y=70)

#BUTTONS 
btn1 = Button(ventana, text="Generar Contraseña", command= generatePassword).place(x=200, y=250)
btn2 = Button(ventana, text="Copiar",command=copy).place(x=370, y=70)

#CHECKBUTTONS OPTIONS
checkVar1 = Checkbutton(frame, text = "ABC", variable = mayus, onvalue = 1, offvalue = 2, height=1, width = 200, anchor="w").pack()
checkVar2 = Checkbutton(frame, text = "abc", variable = minus, onvalue = 1, offvalue = 0, height=1, width = 200, anchor="w").pack()
checkVar3 = Checkbutton(frame, text = "123", variable = numb, onvalue = 1, offvalue = 0, height=1, width = 200, anchor="w").pack()  
checkVar4 = Checkbutton(frame, text = "@#$%", variable = simb, onvalue = 1, offvalue = 0, height=1, width = 200, anchor="w").pack()  

#SPINBOX LENGTH
spin = Spinbox(frame, from_=8, to_=20, textvariable=length, width=5,justify="left")
spin.place(anchor="e")
spin.pack()

ventana.mainloop()
