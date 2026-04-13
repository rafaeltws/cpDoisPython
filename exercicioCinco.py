nome = input('insira seu nome: ')
idade = int(input("sua idade: "))
renda_mensal = float(input("insira sua renda: "))
valor_emprestimo = float(input("valor que gostaria do emprestimo: "))
numero_parcelas = int(input("quantas parcelas conseguiria pagar: "))
juros = 0

if idade >= 18:
    valor_do_financiamento_maximo = renda_mensal * 20
    if valor_emprestimo > valor_do_financiamento_maximo:
        print(f"Reprovado: O valor excede seu limite de R${valor_do_financiamento_maximo}")
        exit()
else:
    print("Reprovado: Menor de idade.")
    exit()

if numero_parcelas <= 6:
    juros = 0.05
elif numero_parcelas <= 12:
    juros = 0.08
elif numero_parcelas <= 24:
    juros = 0.10
else:
    print("ERRO: Número de parcelas inválido (máximo 24).")
    exit()

pmt = valor_emprestimo * (juros * (1 + juros) ** numero_parcelas) / ((1 + juros) ** numero_parcelas - 1)
total_pago = pmt * numero_parcelas
total_juros = total_pago - valor_emprestimo

print("\n=== RESUMO DO EMPRÉSTIMO ===")
print(f"Cliente: {nome}")
print(f"Valor financiado: R$ {valor_emprestimo:.2f}")
print(f"Parcelas: {numero_parcelas}x")
print(f"Taxa de juros: {juros * 100:.0f}% ao mês")
print(f"Valor da parcela: R$ {pmt:.2f}")
print(f"Total a pagar: R$ {total_pago:.2f}")
print(f"Total de juros pagos: R$ {total_juros:.2f}")