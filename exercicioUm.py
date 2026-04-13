# Entrada de dados
estado = int(input("Digite o código do estado de origem (1 a 5): "))
pesoToneladas = float(input("Digite o peso da carga em toneladas: "))
codigoCarga = int(input("Digite o código da carga (10 a 40): "))

pesoKg = pesoToneladas * 1000

if codigoCarga >= 10 and codigoCarga <= 20:
    precoKg = 100
elif codigoCarga >= 21 and codigoCarga <= 30:
    precoKg = 250
elif codigoCarga >= 31 and codigoCarga <= 40:
    precoKg = 340

precoCarga = pesoKg * precoKg

match estado:
    case 1:
        imposto = 0.35
    case 2:
        imposto = 0.25
    case 3:
        imposto = 0.15
    case 4:
        imposto = 0.05
    case 5:
        imposto = 0

valorImposto = precoCarga * imposto

valorTotal = precoCarga + valorImposto

print(f"Peso da carga em kg: {pesoKg:.2f}")
print(f"Preço da carga: R$ {precoCarga:.2f}")
print(f"Valor do imposto: R$ {valorImposto:.2f}")
print(f"Valor total transportado: R$ {valorTotal:.2f}")