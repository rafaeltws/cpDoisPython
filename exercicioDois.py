ladoA = float(input("valor da hipotenusa (lado A): "))
ladoB = float(input("valor do cateto (lado B): "))
ladoC = float(input("valor do cateto (lado C): "))

if ladoA >= ladoB + ladoC:
    print("Não é um triângulo")

else:
    if ladoA == ladoB == ladoC:
        print("TRIANGULO EQUILATERO")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("TRIANGULO ISOSCELES")
    else:
        print("TRIANGULO ESCALENO")


if ladoA**2 == ladoB**2 + ladoC**2:
    print("TRIANGULO RETANGULO")
elif ladoA**2 > ladoB**2 + ladoC**2:
    print("TRIANGULO OBTUSANGULO")
else:
    print("TRIANGULO ACUTANGULO")