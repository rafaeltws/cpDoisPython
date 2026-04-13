notaCpUm = float(input("Digite a sua nota da cp1 (0 a 10)"))
notaCpDois = float(input("Digite a sua nota da cp2 (0 a 10)"))
notaCpTres = float(input("Digite a sua nota da cp3 (0 a 10)"))
notaSprintUm = float(input("Digite a sua nota da sp1 (0 a 10)"))
notaSprintDois = float(input("Digite a sua nota da sp2 (0 a 10)"))
notaGlobalSolution = float(input("Digite a sua nota da Global Solution (0 a 10)"))

def mediaSemMenor(n1, n2, n3):
    menorNota = n1

    if n2 < menorNota:
        menorNota = n2
    elif n3 < menorNota:
        menorNota = n3
    somaMaiores = n1 + n2 + n3 - menorNota

    media = ((somaMaiores + notaSprintUm + notaSprintDois) / 4) * 0.4 + notaGlobalSolution * 0.6
    mediaComPeso = media * 0.4

    return media, mediaComPeso

media, mediaComPeso = mediaSemMenor(notaCpUm, notaCpDois, notaCpTres)

print(f"Média (com peso): {mediaComPeso:.1f}")
print(f"Média : {media:.1f}")
