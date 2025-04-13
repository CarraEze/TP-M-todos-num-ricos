import sympy as sp
def newton(f, x0, variable_str='x'):
    x = sp.symbols(variable_str)
    f_derivada = sp.diff(f,x)

    for i in range(0,10):
        f_x0 = f.subs(x, x0)
        f_derivada_x0 = f_derivada.subs(x, x0)
        x0 = float(x0 - (f_x0 / f_derivada_x0))
    print(f"Nuevo punto: {x0}")

def triseccion(f, a, b, variable_str='x'):
    x = sp.symbols(variable_str)

    for i in range(0,3):
        x1 = a + (b - a) / 3
        x2 = a + 2 * (b - a) / 3
        f_x1 = f.subs(x, x1)
        f_x2 = f.subs(x, x2)

        if f_x1 > f_x2:
            a, b = x1, b
        else:
            a, b = a, x2
    print(f"Nuevo intervalo: [{a}, {b}]")
    newton(f, b)

a = input("Ingrese el punto inicial")
b = input("Ingrese el punto final")
a = sp.sympify(a)
b = sp.sympify(b)
funcion = "x - 430"
f = sp.sympify(funcion)
triseccion(f, a, b)


