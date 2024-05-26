def panelsInRoof(a, b, x, y):
    # Panel en orientación original (a x b)
    panels_orientation_1 = (x // a) * (y // b)
    # Panel en orientación rotada (b x a)
    panels_orientation_2 = (x // b) * (y // a)
    
    # Retornar el máximo de las dos orientaciones
    return max(panels_orientation_1, panels_orientation_2)

# Solicitar inputs del usuario
a = int(input("Ingresa el largo del panel: "))
b = int(input("Ingresa el ancho del panel: "))
x = int(input("Ingresa el largo del techo: "))
y = int(input("Ingresa el ancho del techo: "))

# Calcular y mostrar el resultado
resultado = panelsInRoof(a, b, x, y)
print(f"El número de paneles que caben en el techo es: {resultado}")