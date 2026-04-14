def calcular_horas_extras(salario_base, horas):
   valor = salario_base * 0.015 * horas
   return valor

def calcular_descontos_faltas(salario_base, faltas):
   desconto = salario_base * 0.02 * faltas
   return desconto

def calcular_bonus(cargo, recebeu_bonus):
   if recebeu_bonus == "s":
       if cargo == 1:
           return 1000
       elif cargo == 2:
           return 500
       elif cargo == 3:
           return 300
       elif cargo == 4:
           return 100
   return 0

nome = input("Digite o nome do funcionário: ")
cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Digite o salário base: "))
horas_extras = float(input("Digite o total de horas extras: "))
faltas = int(input("Digite o total de faltas: "))
recebeu_bonus = input("Recebeu bônus? (s/n): ")

valor_horas = calcular_horas_extras(salario_base, horas_extras)
valor_desconto = calcular_descontos_faltas(salario_base, faltas)
valor_bonus = calcular_bonus(cargo, recebeu_bonus)
salario_bruto = salario_base
acrescimos = valor_horas + valor_bonus
descontos = valor_desconto
salario_final = salario_bruto + acrescimos - descontos

print("Funcionário:", nome)
print("Salário bruto:", salario_bruto)
print("Acréscimos:", acrescimos)
print("Descontos:", descontos)
print("Salário final:", salario_final)
