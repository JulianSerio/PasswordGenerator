#Password generator
from tkinter import *
from tkinter import messagebox
import random
import tkinter 
import tkinter.ttk as ttk

#GENERATE 
def generatePassword():
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "`~!@#$%^&*()-=]}{[]\|':;,.></?"
    ans = ""
    if (mayus.get()==1):    #IF mayus IS PRESSED 
        ans = ans + mayusculas  #ADD mayusculas
        if (minus.get()==1):        #IF minus IS PRESSED 
            ans = ans + minusculas     #ADD minuscula   
            if (numb.get()==1):            #IF numb IS PRESSED
                ans = ans + numeros           #ADD numeros
            elif (simb.get()==1):          #ELSE
                ans = ans + simbolos          #ADD simbolos
                 
        elif (numb.get()==1):
            ans = ans + numeros 
            if (minus.get()==1):
                ans = ans + minusculas  
            elif (simb.get()==1):
                ans = ans + simbolos

        elif (simb.get()==1):
            ans = ans + simbolos 
            if (numb.get()==1):
                    ans = ans + numeros     
            elif (minus.get()==1):
                ans = ans + minusculas

    elif (minus.get()==1):
        ans = ans + minusculas 
        if (mayus.get()==1):
            ans = ans + mayusculas
            if (numb.get()==1):
                ans = ans + numeros     
            elif (simb.get()==1):
                ans = ans + simbolos 

        elif (numb.get()==1):
            ans = ans + numeros
            if (mayus.get()==1):
                ans = ans + mayusculas
            elif (simb.get()==1):
                ans = ans + simbolos 

        elif (simb.get()==1):
            ans = ans + simbolos 
            if (mayus.get()==1):
                ans = ans + mayusculas
            elif (numb.get()==1):
                ans = ans + numeros     

    elif (numb.get()==1):
        ans = ans + numeros
        if (minus.get()==1):
            ans = ans + minusculas
            if (mayus.get()==1):
                ans = ans + mayusculas
            elif (simb.get()==1):
                ans = ans + simbolos

        elif (mayus.get()==1):
            ans = ans + mayusculas
            if (minus.get()==1):
                ans = ans + minusculas
            elif (simb.get()==1):
                ans = ans + simbolos 

        elif (simb.get()==1):
            ans = ans + simbolos 
            if (mayus.get()==1):
                ans = ans + mayusculas
            elif (minus.get()==1):
                ans = ans + minusculas

    elif (simb.get()==1):
        ans = ans + simbolos
        if (numb.get()==1):
            ans = ans + numeros 
            if (mayus.get()==1):
                ans = ans + mayusculas
            elif (minus.get()==1):
                ans = ans + minusculas
        elif (minus.get()==1):
            ans = ans + minusculas
            if (mayus.get()==1):
                ans = ans + mayusculas
            elif (numb.get()==1):
                ans = ans + numeros  

        elif (mayus.get()==1):
            ans = ans + mayusculas 
            if (numb.get()==1):
                ans = ans + numeros     
            elif (minus.get()==1):
                ans = ans + minusculas
    else:   
        ans = minusculas + mayusculas + numeros + simbolos
        
    ans = "".join(random.sample(ans,length.get())) #RANDOMIZE
    etiqueta = password.set(ans) #MOSTRAR
    
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