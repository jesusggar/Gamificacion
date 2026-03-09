def f(x):
    """Función a integrar: f(x) = x^3"""
    return x**3

def integral_exacta(a, b):
    """Primitiva evaluada: F(x) = (x^4) / 4"""
    return (b**4 / 4) - (a**4 / 4)

def metodo_rectangulos(a, b, n):
    """Aproximación por la izquierda"""
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        x = a + i * dx
        suma += f(x) * dx
    return suma

def metodo_trapecios(a, b, n):
    dx = (b - a) / n
    # Sumamos el primer y último término divididos por 2
    suma = 0.5 * (f(a) + f(b)) 
    for i in range(1, n):
        x = a + i * dx
        suma += f(x)
    return suma * dx

def metodo_simpson(a, b, n):
    # Simpson requiere que 'n' sea un número par de intervalos
    if n % 2 != 0:
        n += 1 
        
    dx = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * dx
        if i % 2 == 0:
            suma += 2 * f(x)
        else:
            suma += 4 * f(x)
            
    return suma * dx / 3


# --- COMPARATIVA DE PRECISIÓN ---
a, b = 0, 2
valor_exacto = integral_exacta(a, b)
intervalos = [4, 10, 50, 100]

print(f"Valor Exacto Analítico: {valor_exacto}\n")

for n in intervalos:
    print(f"--- Evaluando con n = {n} intervalos ---")
    
    res_rect = metodo_rectangulos(a, b, n)
    err_rect = abs(valor_exacto - res_rect)
    print(f"Rectángulos : {res_rect:.6f} | Error: {err_rect:.6f}")
    
    res_trap = metodo_trapecios(a, b, n)
    err_trap = abs(valor_exacto - res_trap)
    print(f"Trapecios   : {res_trap:.6f} | Error: {err_trap:.6f}")
    
    res_simp = metodo_simpson(a, b, n)
    err_simp = abs(valor_exacto - res_simp)
    print(f"Simpson     : {res_simp:.6f} | Error: {err_simp:.6f}\n")