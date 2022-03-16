
# Primeira parte: Apenas IMC
nome = "Pedro"
idade = 19
altura = 1.90
peso = 90
imc = peso / (altura ** 2)

print(f'{nome} "tem" {idade} "anos de idade e seu IMC equivale a:" {imc:.2f}')
print('{} tem {} anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))

print()

# Segunda parte: IMC + Descobrir data de nascimento
nome = "Pedro"
idade = 19 
altura = 1.90
peso = 90
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / (altura ** 2)
print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.")
print(f"O IMC de {nome} equivale a {imc:.2f}")
print(f"{nome} nasceu em {nascimento}.")




