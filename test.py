import sympy as sy

def cuadrado(x1,x2,n):
    for i in range (0,n):
        x2 = x2*x1
        print(x2)

def iterar(x,x1,y,n):
    for i in range(0,n):
        x = x1 -(y.subs(x1)/y.diff(x).subs(x1))
        x1 = x
    return x

x = sy.Symbol("x")
x1 = sy.sympify(input("Ingrese un numero como punto de inicio"))
x2 = 1
y = sy.sympify(input("ingresa tu funcion "))
n = sy.sympify(input("ingresa un numero de iteraciones"))
print(iterar(x1,x2,y,n))

