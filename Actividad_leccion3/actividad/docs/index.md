# Bienvenido a calculadora con Tkinter

Aquí se encuentra la información necesaria para comprender cómo funciona una calculadora implementada con la ayuda de Tkinter.

## Sobre el funcionamiento de la calculadora

Esta calculadora utiliza dos números introducidos por el usuario por pantalla (N1 y N2), y mediante un botón, realiza la operación deseada. En el caso de que la operación solo necesite de un operando, el introducido deberá ser N1.
Es necesario tener instalado Tkinter, para ello:
```bash
pip install tkinter
```

## Métodos

  - ***sumar()***:
      Aplica una suma a n1 y n2 (n1+n2).
      **Input**: n1 y n2 introducidos por pantalla.
      **Output**: r, resultado de la suma.
  - ***restar()***:
      Aplica una resta a n1 y n2 (n1-n2).
      **Input**: n1 y n2 introducidos por pantalla.
      **Output**: r, resultado de la resta.
  - ***multiplicar()***:
      Aplica una multiplicación a n1 y n2 (n1*n2).
      **Input**: n1 y n2 introducidos por pantalla.
      **Output**: r, resultado de la multiplicación.
  - ***dividir()***:
      Aplica una división a n1 y n2 (n1/n2).
      **Input**: n1 y n2 introducidos por pantalla.
      **Output**: r, resultado de la división.
  - ***potencia()***:
      Eleva n1 a la potencia n2 (n1^n2).
      **Input**: n1 introducido por pantalla.
      **Output**: r, resultado de la potencia.
  - ***cuadrado()***:
      Eleva al cuadrado n1 (n1^2).
      **Input**: n1 introducido por pantalla.
      **Output**: r, resultado del cuadrado.
  - ***raiz_cuadrada()***:
      Aplica raíz cuadrada a n1 (sqrt(n1)).
      **Input**: n1 introducido por pantalla.
      **Output**: r, resultado de la raíz cuadrada.
  - ***inversa()***:
      Calcula la inversa de n1 (1/n1).
      **Input**: n1 introducido por pantalla.
      **Output**: r, resultado de la inversa.
  - ***borrar()***:
      Elimina los valores de n1 y n2.
  - ***clear()***:
      Elimina el valor de r.
  - ***mensaje()***:
      Genera un mensaje para informar al usuario de que para utilizar las funciones cuadrado, raiz_cuadrada e inversa, solo tiene que introducir n1.

## Sobre la construcción de la calculadora

En este apartado encontramos algunos ejemplos comentados para comprender mejor la construcción de la calculadora.

    # Ejemplo construcción de casillas para introducir los valores de n1 y n2.

    label_n1 = Label(root, text="Número 1", bg="black", fg="light grey")  # Etiqueta explicativa de la casilla donde se introducirá N1.
    label_n1.place(x=220, y=30)  # Posición de la etiqueta anterior.
    entrada1 = Entry(root, textvariable=n1, bg="royal blue")  # Casilla para intoriducir por pantalla N1.
    entrada1.place(x=185, y=60)  # Posición de casilla anterior.


    # Ejemplo de la construcción del botón y etiqueta explicativa en la calculadora.
    boton_suma = Button(root, text="SUMA", bg="RoyalBlue1", command=sumar)  # Creación del botón para sumar N1 y N2, donde también se especifica el método que hay qye llamar al pulsar el botón.
    boton_suma.place(x=20, y=260)  # Posición del botón.
    Label(root, text="(N1+N2)", bg="black", fg="gray").place(x=15, y=288)  # Etiqueta explicativa de lo que hace el botón.
