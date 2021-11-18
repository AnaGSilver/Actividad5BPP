from tkinter import *
from tkinter import messagebox as MessageBox


def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()


def restar():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()


def multiplicar():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()


def dividir():
    r.set(float(n1.get()) / float(n2.get()))
    borrar()


def potencia():
    r.set(float(n1.get()) ** float(n2.get()))
    borrar()


def cuadrado():
    r.set(float(n1.get()) ** 2)
    if n2.get() != '':
        mensaje()
    borrar()


def raiz_cuadrada():
    r.set(float(n1.get()) ** 0.5)
    if n2.get() != '':
        mensaje()
    borrar()


def inversa():
    r.set(1 / float(n1.get()))
    if n2.get() != '':
        mensaje()
    borrar()


def borrar():
    n1.set('')
    n2.set('')


def clear():
    r.set('')

def mensaje():
    MessageBox.showinfo('Información', 'Para usar las funciones "Cuadrado", "Raíz cuadrada" e "Inversa", debes introducir solo un número en la casilla "Número 1".')


root = Tk()


root.title("Calculadora")
root.resizable(0, 0)
root.geometry("500x420")
root.config(bg="black")

n1 = StringVar()
n2 = StringVar()
r = StringVar()

label_n1 = Label(root, text="Número 1", bg="black", fg="light grey")
label_n1.place(x=220, y=30)
entrada1 = Entry(root, textvariable=n1, bg="royal blue")
entrada1.place(x=185, y=60)

label_n2 = Label(root, text="Número 2", bg="black", fg="light grey")
label_n2.place(x=220, y=90)
entrada2 = Entry(root, textvariable=n2, bg="royal blue")
entrada2.place(x=185, y=120)

label_r = Label(root, text="Resultado", bg="black", fg="gray", font=('bold'))
label_r.place(x=205, y=180)
entrada_r = Entry(root, textvariable=r, bg="RoyalBlue4", fg="white", font=(20),
                  justify='center')
entrada_r.place(x=138, y=210)

boton_suma = Button(root, text="SUMA", bg="RoyalBlue1", command=sumar)
boton_suma.place(x=20, y=260)
Label(root, text="(N1+N2)", bg="black", fg="gray").place(x=15, y=288)
boton_resta = Button(root, text="RESTA", bg="RoyalBlue1", command=restar)
boton_resta.place(x=100, y=260)
Label(root, text="(N1-N2)", bg="black", fg="gray").place(x=97, y=288)
boton_multiplicacion = Button(root, text="MULTIPLICACION", bg="RoyalBlue1", command=multiplicar)
boton_multiplicacion.place(x=180, y=260)
Label(root, text="(N1xN2)", bg="black", fg="gray").place(x=207, y=288)
boton_division = Button(root, text="DIVISION", bg="RoyalBlue1", command=dividir)
boton_division.place(x=320, y=260)
Label(root, text="(N1/N2)", bg="black", fg="gray").place(x=324, y=288)
boton_potencia = Button(root, text="POTENCIA", bg="RoyalBlue1", command=potencia)
boton_potencia.place(x=415, y=260)
Label(root, text="(N1^N2)", bg="black", fg="gray").place(x=422, y=288)
boton_cuadrado = Button(root, text="CUADRADO", bg="RoyalBlue1", command=cuadrado)
boton_cuadrado.place(x=70, y=340)
Label(root, text="(N1^2)", bg="black", fg="gray").place(x=87, y=368)
boton_raiz = Button(root, text="RAIZ CUADRADA", bg="RoyalBlue1", command=raiz_cuadrada)
boton_raiz.place(x=170, y=340)
Label(root, text="(sqrt(N1))", bg="black", fg="gray").place(x=195, y=368)
boton_inversa = Button(root, text="INVERSA", bg="RoyalBlue1", command=inversa)
boton_inversa.place(x=295, y=340)
Label(root, text="(1/N1)", bg="black", fg="gray").place(x=302, y=368)
boton_clear = Button(root, text="C", bg="RoyalBlue1", command=clear)
boton_clear.place(x=410, y=340)


root.mainloop()
