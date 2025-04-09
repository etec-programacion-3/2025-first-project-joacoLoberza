def circlePerimeter (radius):
    perimeter = 2*3.1416*radius
    return perimeter
def squerePerimeter (side):
    perimeter = 4*side
    return perimeter
radius = float(input("Introduzca el radio del círculo:\n"))
perimeter = circlePerimeter(radius)
print("El perímetro del círculo es: ", perimeter)

side = float(input("Introduzca el lado del cuadrado:\n"))
perimeter = squerePerimeter(side)
print("El perímetro del cuadrado es: ", perimeter)